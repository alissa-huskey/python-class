from pathlib import Path

from docutils import nodes
from docutils.core import publish_doctree
import pytest

from docs._ext.fieldlist import Field

rootdir = Path(__file__).parent
datadir = rootdir/"tests"/"roots"/"fieldlists"

def xml_field(tag, contents):
    if not contents:
        return f"<field_{tag}/>"
    return f"<field_{tag}>{contents}</field_{tag}>"

@pytest.fixture()
def params(request):
    try:
        params = request.param
    except AttributeError:
        params = {}

    name_xml = params.pop("name_xml", params["name"])
    body_xml = params.pop("body_xml", None)

    if params["body"] and not body_xml:
        body_xml = f"<paragraph>{params['body']}</paragraph>"

    params["xml"] = (
        "<field>" +
        xml_field("name", name_xml) +
        xml_field("body", body_xml) +
        "</field>"
    )

    return params


@pytest.mark.parametrize("params",
    [
        dict(
            text=":version: 0.0.1",
            name="version",
            body="0.0.1",
        ),
        dict(
            text=":multiword field: hello",
            name="multiword field",
            body="hello",
        ),
        dict(
            text=":*Note*: deprecated",
            name="*Note*",
            body="deprecated",
            name_xml="<emphasis>Note</emphasis>",
        ),
        dict(
            text=":flag: ",
            name="flag",
            body="",
        ),
        dict(
            text="""
                :Address: 123 Example Ave.
                          Example, EX
            """.strip(),
            name="Address",
            body="123 Example Ave.\nExample, EX",
        ),
        dict(
            text=":class: `Path`",
            name="class",
            body="`Path`",
            body_xml="<paragraph><literal>Path</literal></paragraph>"
        ),
        dict(
            text=":logo: ![](images/logo.png)",
            name="logo",
            body="![](images/logo.png)",
            body_xml='<paragraph><image alt="" uri="images/logo.png"/></paragraph>'
        ),
        dict(
            text="""
                :thanks-to:
                    - Tony J. (Tibs) Ibbs
                    - David Goodger
            """.strip(),
            name="thanks-to",
            body="- Tony J. (Tibs) Ibbs\n- David Goodger",
            body_xml=(
                "<bullet_list>"
                "<list_item><paragraph>Tony J. (Tibs) Ibbs</paragraph></list_item>"
                "<list_item><paragraph>David Goodger</paragraph></list_item>"
                "</bullet_list>"
            )
        ),
    ],
    indirect=True
)
def test_field(params):
    text, name, body, xml = params.values()

    doc = publish_doctree(f"# title\n\n{text}")
    fields = list(doc.traverse(nodes.field))

    assert len(fields) == 1

    field = Field(fields[0])
    field.transform()

    assert field.name == name, f'field.name failure given raw source "{text}"'
    assert field.body == body, f'field.body failure given raw source "{text}"'
    assert field.toxml() == xml, f'field.toxml() failure given raw source "{text}"'
