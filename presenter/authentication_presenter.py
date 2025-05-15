from PySide6.QtCore import QObject, Signal # type: ignore
from view.authentication_view import AuthenticationView

class AuthenticationPresenter(QObject):
    signal_authentication_success = Signal()

    def __init__(self):
        super().__init__()
        self.authentication_view = AuthenticationView()
        self.authentication_view.signal_authentication_success.connect(self._on_authentication_success)

    def show_view(self):
        self.authentication_view.show()

    def _on_authentication_success(self):
        self.signal_authentication_success.emit()