

# QuoteFusion - Quote Generation using LSTM


## Overview

**QuoteFusion** is an NLP-based project that generates inspiring and insightful quotes using a Long Short-Term Memory (LSTM) neural network. The model is trained on a curated dataset of famous quotes, literary texts, and aphorisms, capturing patterns in language to create unique and contextually relevant quotes. This project demonstrates the application of deep learning in creative content generation.

## Features

- **LSTM Model**: Utilizes an LSTM neural network to generate quotes based on learned patterns in the training data.
- **Data Preprocessing**: Includes Data is scraped from the web, text cleaning, tokenization, and sequence padding to prepare data for the model.
- **Customizable Generation**: Users can specify the length and theme of the quotes.

🟢 Click on the image to see the demo video:

[![QuoteFusion](https://github.com/aakashmohole/QuoteFusion-Quote-Genration-using-LSTM/blob/main/img.png)](https://youtu.be/0h5OpzB5DPg)

### Web Interface

1. Run the jupyter file then from last cell click on url to redirect to the deployed Gradio interface.
2. Enter a prompt to generate a quote.
3. Explore the generated quotes and their diversity.



## Installation

To set up the project locally, follow these steps:

**Clone the repository**:

```bash
 git clone  https://github.com/aakashmohole/QuoteFusion-Quote-Genration-using-LSTM.git
 ```


### Example
- **Python**
```python
from gradio_client import Client

client = Client("https://8a60bc40aabf89f175.gradio.live/")
result = client.predict(
		Prompt="Hello!!",
		nwords=13,
		api_name="/predict"
)
print(result)
```

- **JavaScript**
```javascript
import { Client } from "@gradio/client";

const client = await Client.connect("https://8a60bc40aabf89f175.gradio.live/");
const result = await client.predict("/predict", { 		
		Prompt: "Hello!!", 		
		nwords: 10, 
});

console.log(result.data);
```

- **Bash**
```bash
curl -X POST https://8a60bc40aabf89f175.gradio.live/call/predict -s -H "Content-Type: application/json" -d '{
  "data": [
    "Hello!!",
    10
]}' \
  | awk -F'"' '{ print $4}'  \
  | read EVENT_ID; curl -N https://8a60bc40aabf89f175.gradio.live/call/predict/$EVENT_ID
```



## Contributing 🤝

Contributions are welcome! Please fork the repository and create a pull request with your improvements.


How to reach me: Connect with me on Twitter [@Aakash Mohole](https://twitter.com/AakashMohole) | Linkedin [@Aakash Mohole](https://www.linkedin.com/in/aakash-mohole-231359233/)
