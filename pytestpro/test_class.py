class TestClass:

    """

    you can't write the __init__ method inside a Test* class. it will cause
    PytestCollectionWarning: cannot collect test class 'TestClass' because it has a __init__ constructor (from: test_class.py)
    class TestClass:

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

    """

    # def __init__(self):
    #     pass
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert 3==3
