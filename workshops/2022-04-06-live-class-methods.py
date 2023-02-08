"""
2022-04-06 -- Data & In-Depth: Class methods (vs. instance methods)

Attendees
---------

- Jayson
- Brian

"""

class Thing:
    
    @classmethod
    def do_classy_thing(cls):
        print("Doing the thing.")
        
    def do_thing(self):
        print("doing the thing")


# instantiate a Thing object

this_thing = Thing()

# call a method on the instance

this_thing.do_thing()

# call the method on the Thing class
#      but you need to pass an argument to stand in for self

Thing.do_thing(None)

# also call the method on the Thing class
# .    but in a very round-about way of accessing
#      __class__ on the instance (to get Thing), then
#      manually passing the instance as self

this_thing.__class__.do_thing(this_thing)

# calls the class method on the class
#       here, cls = Thing

Thing.do_classy_thing()

# call the class method on the instance
#       here, cls = self

this_thing.do_classy_thing()


class App():
    
    # class property
    debug_mode = True
    
    # class method that sets the property on the class
    @classmethod
    def set_debug(cls, is_debug):
        cls.debug_mode = is_debug

    # instance method that looks at the property set on the class
    def debug(self, message):
        if not self.debug_mode:
            return
        
        print("Debug>", message)

# calling a class method on the class
#   applies to the class, therefore all instances

App.set_debug(False)

app = App()

# calling a class method on an instance
#   still applies to the class, therefore all instances

app.set_debug(False)

print("Class debug mode:", App.debug_mode)
print("Instance debug mode:", app.debug_mode)

other_app = App()

# calling a class method on an instance, again
#   STILL applies to the class, therefore all instances
#   (though set_debug() was only called on app, it is also
#    changed on other_app)

app.set_debug(True)

print("app debug mode:", app.debug_mode)
print("other_app debug mode:", other_app.debug_mode)


class Car():
    
    # good -- you would want a recall to apply to all instances

    @classmethod
    def set_recall(cls):
        cls.is_recalled = True

        
    # bad -- if you changed the color on one car to red,
    #        you wouldn't want all cars to be red

    @classmethod
    def set_color(cls, color):
        cls.color = color

    
    # good -- you would want an instance method here
    
    def set_color(self, color):
        self.color = True