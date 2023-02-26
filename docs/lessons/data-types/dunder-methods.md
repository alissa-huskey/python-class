
### Operator dunder methods

Below are tables matching operators to their corresponding dunder methods.

#### Arithmetic Operators

| Operator | Meaning                   | Method          | Operator | Method          |
|----------|---------------------------|-----------------|----------|-----------------|
| `+`      | sum                       | `__add__`       | `+=`     | `__iadd__`      |
| `-`      | difference                | `__sub__`       | `-=`     | `__isub__`      |
| `*`      | product                   | `__mul__`       | `*=`     | `__imul__`      |
| `/`      | quotient                  | `__truediv__`   | `/=`     | `__itruediv__`  |
| `//`     | floored quotient          | `__floordiv__`  | `//=`    | `__ifloordiv__` |
| `%`      | remainder                 | `__mod__`       | `%=`     | `__imod__`      |
| `**`     | power of                  | `__pow__`       | `**=`    | `__ipow__`      |

#### Comparison operators

| Operator | Meaning                   | Method          |
|----------|---------------------------|-----------------|
| `<`      | less than                 | `__lt__`        |
| `>`      | greater than              | `__gt__`        |
| `<=`     | less than or equal to     | `__le__`        |
| `>=`     | greater than or equal to  | `__ge__`        |
| `==`     | equals                    | `__eq__`        |
| `!=`     | not equals                | `__nq__`        |
| `in`     | contains                  | `__contains__`  |

