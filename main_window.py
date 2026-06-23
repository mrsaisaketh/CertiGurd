from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QLabel,
    QPushButton, QFileDialog, QFrame, QHBoxLayout,
    QProgressBar
)
from PyQt6.QtCore import Qt, QPropertyAnimation
from PyQt6.QtGui import QFont
from core.verifier import verify_certificate


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CertiGuard")
        self.resize(1000, 720)
        self.file_path = None

        self.setStyleSheet("""
            QWidget {
                background-color: qlineargradient(
                    x1:0, y1:0, x2:1, y2:1,
                    stop:0 #141E30,
                    stop:1 #243B55
                );
                color: white;
                font-family: Segoe UI;
            }

            QPushButton {
                background-color: #3A7AFE;
                border-radius: 12px;
                padding: 14px;
                font-size: 15px;
            }

            QPushButton:hover {
                background-color: #5A8CFF;
            }

            QFrame {
                background-color: rgba(255,255,255,0.08);
                border-radius: 18px;
                padding: 25px;
            }

            QProgressBar {
                border-radius: 8px;
                background-color: #222;
            }

            QProgressBar::chunk {
                background-color: #3A7AFE;
                border-radius: 8px;
            }
        """)

        main_layout = QVBoxLayout()

        # Title
        title = QLabel("🛡 CertiGuard")
        title.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(title)

        subtitle = QLabel("AI + Blockchain Certificate Verification")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(subtitle)

        # Buttons
        button_layout = QHBoxLayout()

        self.upload_btn = QPushButton("Upload Certificate")
        self.upload_btn.clicked.connect(self.upload_file)

        self.verify_btn = QPushButton("Verify Now")
        self.verify_btn.clicked.connect(self.verify)
        self.verify_btn.setEnabled(False)

        button_layout.addWidget(self.upload_btn)
        button_layout.addWidget(self.verify_btn)

        main_layout.addLayout(button_layout)

        # Loading bar
        self.progress = QProgressBar()
        self.progress.setVisible(False)
        main_layout.addWidget(self.progress)

        # Result Card
        self.result_card = QFrame()
        self.result_card.setVisible(False)

        self.status_label = QLabel("")
        self.status_label.setFont(QFont("Segoe UI", 16))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        card_layout = QVBoxLayout()
        card_layout.addWidget(self.status_label)
        self.result_card.setLayout(card_layout)

        main_layout.addWidget(self.result_card)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def upload_file(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Select Certificate", "", "Images (*.png *.jpg *.jpeg *.pdf)"
        )
        if file:
            self.file_path = file
            self.verify_btn.setEnabled(True)

    def verify(self):

        self.progress.setVisible(True)
        self.progress.setValue(30)

        result_text, status = verify_certificate(self.file_path)

        self.progress.setValue(100)

        # Status Color Badge
        if "ORIGINAL" in status:
            color = "#2ECC71"
        elif "FAKE" in status:
            color = "#E74C3C"
        else:
            color = "#F39C12"

        self.status_label.setStyleSheet(f"""
            font-size:18px;
            padding:20px;
            border:3px solid {color};
            border-radius:15px;
        """)

        self.status_label.setText(result_text)
        self.result_card.setVisible(True)

        # Fade-in Animation
        self.animation = QPropertyAnimation(self.result_card, b"windowOpacity")
        self.animation.setDuration(500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        self.progress.setVisible(False)