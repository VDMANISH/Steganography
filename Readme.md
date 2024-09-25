# Steganography.
1) Steganography as an information security method hides data or a message within another file, non-elusive file thus masking the evidence of the hidden information. 
2) Steganography, by contrast, is concerned with hiding the message itself and the mere existence of the message from anyone, including the one who possesses the message and in such cases, encryption is not necessary. 
3) It can also be employed in text, images, or videos.
4) In this project, we'll concentrate on a text-based steganography. The secret is hidden within the text itself by continuously editing the text in a text document by inserting spaces or tabs in a certain pattern.

# Structure: 
steganography/
│
├── src/                  # Source code for the project
│   ├── encoder.py        # encoding secret messages
│   ├── decoder.py        # decoding hidden messages
│   └── utils.py          # Utility functions for the project
│
├── data/                 # data for testing
│   ├── cover_text.txt    # cover text file
│   └── secret_message.txt # secret message file
│
├── tests/                # Test cases for validation
│   ├── test_encoder.py    # Tests for the encoder
│   └── test_decoder.py    # Tests for the decoder
│
├── README.md             # Project documentation
├── LICENSE               # License information
└── requirements.txt      # Required Python packages

![image](https://github.com/user-attachments/assets/42db7087-5486-4bba-ad1b-1eed51233be1)
