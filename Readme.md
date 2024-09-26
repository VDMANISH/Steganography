# Steganography.
1) Steganography as an information security method hides data or a message within another file, non-elusive file thus masking the evidence of the hidden information. 
2) Steganography, by contrast, is concerned with hiding the message itself and the mere existence of the message from anyone, including the one who possesses the message and in such cases, encryption is not necessary. 
3) It can also be employed in text, images, or videos.
4) In this project, we'll concentrate on a text-based steganography. The secret is hidden within the text itself by continuously editing the text in a text document by inserting spaces or tabs in a certain pattern.

  ![image](https://github.com/user-attachments/assets/a553b2c9-88d1-4622-947d-efdb2c8728ff)

# Structure: 
```
steganography/
│
├── src/              # Source code - main one
│ ├── encoder.py      # encoding secret messages
│ ├── decoder.py      # decoding hidden messages
│ └── utils.py        # Utility functions for the project
│
├── data/             # Sample data for testing
│ ├── cover_text.txt  # cover text file
│ └── secret_message.txt # secret message file
│
├── tests/            # Test cases for validation
│ ├── test_encoder.py # Tests for the encoder
│ └── test_decoder.py # Tests for the decoder
│
├── README.md         # Project documentation
├── LICENSE           # License information
└── requirements.txt  # Required Python packages
```

# Current Usage:
In today's world, it plays a significant role in various fields, especially for validation and ensuring uniqueness. Modern steganography often works in combination with cryptography, where the hidden message is first encrypted using cryptographic algorithms and then embedded within a cover medium. Only the intended recipient, equipped with the correct decryption tools, can access the concealed message.

# Types:
Steganography can be broadly divided into two types:

Physical Steganography: In this type, both the secret message and the cover medium are physical objects, such as handwritten notes or printed materials. These items can be physically touched and handled.

Digital Steganography: This method involves hiding data in digital formats. The hidden content and the cover medium consist of binary data (0s and 1s), created using computers or machines. In digital steganography, the general formula is:

`(Secret object + Stego medium + Stego key) = Stego object`

Secret Object: The information that needs to be hidden, such as text, images, or audio.
Stego Medium: The medium used to conceal the secret, which could be a text file, audio file, or image.
Stego Key: The process or method used to hide the secret within the stego medium.

# Modern Digital Steganography Techniques:
Steganography techniques have evolved significantly, and modern digital methods can be categorized based on the type of media used for concealment:

1) Text Steganography: Hiding messages within written text.

2) Image Steganography: Embedding secrets in images.

3) Audio Steganography: Concealing information in sound files.

4) Video Steganography: Hiding data in video files.

5) Network Steganography: Concealing messages within network protocols or traffic.

Combining steganography with cryptography provides even more secure ways to transmit sensitive data, ensuring both confidentiality and undetectability.
