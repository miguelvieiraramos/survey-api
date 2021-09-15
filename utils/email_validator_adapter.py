from presentation.protocols.email_validator import EmailValidator
import validators


class EmailValidatorAdapter(EmailValidator):

    def is_valid(self, email: str) -> bool:
        return validators.email(email)
