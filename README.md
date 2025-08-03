# Neural Style Transfer

Welcome to the **Neural Style Transfer** project! This repository contains an implementation of the Neural Style Transfer algorithm, which allows you to combine the content of one image with the artistic style of another, creating visually stunning results. This project is perfect for those interested in deep learning, computer vision, and generative art.

## Table of Contents
- [About](#about)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## About
Neural Style Transfer (NST) is a technique that uses convolutional neural networks (CNNs) to transfer the artistic style of one image (e.g., a painting) onto the content of another image (e.g., a photograph). This project implements NST using Python and popular deep learning frameworks, enabling users to create unique, stylized images.

The algorithm is based on the seminal work by Gatys et al. (2015), leveraging pre-trained CNNs like VGG to extract content and style features, which are then optimized to produce the final image.

## Features
- Apply artistic styles from one image to the content of another.
- Customizable parameters for balancing content and style weights.
- Support for various pre-trained neural network models (e.g., VGG19).
- Easy-to-use command-line interface for generating stylized images.
- Example scripts and sample images to get started quickly.

## Installation
To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Shudharshan07/Neural-Style-Transfer.git
   cd Neural-Style-Transfer
   ```

2. **Set up a virtual environment** (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the Neural Style Transfer algorithm, use the following command:

```bash
python nst.py --content <path_to_content_image> --style <path_to_style_image> --output <output_image_name>
```

### Example
```bash
python nst.py --content images/content.jpg --style images/style.jpg --output output/stylized_image.jpg
```

### Options
- `--content`: Path to the content image.
- `--style`: Path to the style image.
- `--output`: Path to save the stylized output image.
- `--iterations`: Number of optimization iterations (default: 1000).
- `--content-weight`: Weight for content loss (default: 1e4).
- `--style-weight`: Weight for style loss (default: 1e10).

Run `python nst.py --help` for a full list of options.

## Examples
Here are some example results generated using this project:

- **Content Image**: A photograph of a cityscape.
- **Style Image**: Van Gogh's *Starry Night*.
- **Result**: A cityscape rendered in the style of *Starry Night*.

*Note*: Sample content and style images are provided in the `images/` directory.

## Requirements
The project requires the following dependencies:
- Python 3.6+
- PyTorch
- NumPy
- Pillow
- Matplotlib

Install them using:
```bash
pip install torch numpy pillow matplotlib
```

For the full list, see `requirements.txt`.

## Contributing
Contributions are welcome! If you'd like to contribute, please follow these steps:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Please ensure your code follows the project's coding standards and includes appropriate documentation.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Happy stylizing! If you have any questions or issues, feel free to open an issue on GitHub.
