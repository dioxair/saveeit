<h1 align="center">
  saveeit
  
  ![demonstration](https://dioxair.needs.rest/r/saveeit.gif)
</h1>

## Download Reddit hosted videos your UNIX terminal!

# Requirements:

`Python 3.10.4`
<<<<<<< HEAD

`git`

`A UNIX terminal (Linux, macOS, etc.)`
=======
`git`
`A UNIX terminal (Linux, macOS, etc.)
>>>>>>> aa9bccb1684560d61c2e8ce2be8b3b0515b698af

# Installation

Clone the repository and change the directory to the downloaded repository

```console
git clone https://github.com/samuelolagunju/saveeit.git && cd saveeit
```

After that, install the libraries that `saveeit` uses

```console
python3 -m pip install -r requirements.txt
```

And you're ready to go!

# Usage (part 1)
You can run `saveeit` with

```console
python3 saveeit.py
```

# Usage (part 2)

Optionally, you can make `saveeit` a global command so you can execute it anywhere in your UNIX system with this command:

```console
chmod +x saveeit.py && sudo cp saveeit.py /bin
```

And then you can run it anywhere with

```console
saveeit.py
```
