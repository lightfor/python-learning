class Hello:
    """hello class"""
    @staticmethod
    def print_hello():
        """print hello world"""
        print("hello world!")


print(Hello.__doc__)
print(Hello.print_hello.__doc__)