## Functionality
A function ```parse``` parses the given file and create a scatter plot with CleanBid, CleanAsk and Last Price against the Issuance Date.

| Field Names | Details |
|-------------|----------|
| Issuance Date | a string prefixed wtih **DIs** |
| CleanBid | a number prefixed with **BPr** | 
| CleanAsk | a number prefixed with **APl** |
| Last Price | a number prefixed with **Pl** |

A function ```display``` visualizes the data from a parsed file

## Technical choices
_Matplotlib_ is used for visualization because the library makes it easier to customize style and layout, and it provides a wide range of plots including scatter plot.

## Trade-offs
* The dates could have been formatted better. 'DD-Month-YY'
* The interval or x-axis could have been narrower.

## Visualization
The visualization of the ```example.txt``` file<br />
![Figure_1](https://user-images.githubusercontent.com/39171224/154821293-59348ab0-6e62-4598-8aec-12d969735c01.png)


## How to Execute
### For Windows
Upgrade pip before installing Matplotlib

``` pip install --upgrade pip```


Install Matplotlib

```pip install matplotlib```

Execute the python file ```parse.py```

```python parse.py```

or

```python3 parse.py```
