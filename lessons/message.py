"""Class to store a message (operator overload, union types, default parameters)."""

class Email:

    to: str
    message: str
    important: bool

    def __init__(self, recipient: str | int, message_text: str = "", importance_flag: bool = False) -> None: # initialize the attributes of the object
        # we are defaulting default as false, because most emails are not that important, and we are making the message an empty string
        # | = works for either of those types
        """Constructor of an email."""

        self.to = recipient
        self.message = message_text
        self.important = importance_flag

    def __str__(self) -> str: # returns a string representation of the object
        m_string: str = f"To: {self.to} \n"
        m_string += f"Important? {self.important} \n"
        m_string += f'"{self.message}"'

        return m_string
    
    def __mul__(self, factor: int): # mul is the key word, mul means multiplication
        self.message *= factor # it will repeat that many times

email_to_chiara: Email = Email("chiara", "You're a great TA!", False)
email_to_chiara * 100
print(email_to_chiara)

email_to_lauren: Email = Email("lauren", "Great job!") # if I don't say the importance fla it is False
email_to_lauren: Email = Email(123)
print(email_to_lauren)