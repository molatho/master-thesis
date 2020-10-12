# Master Thesis

## Compilation
On Ubuntu (or any Debian based distro) execute:
```
sudo snap install --classic code
sudo apt install texlive latexmk chktex texlive-latex-extra texlive-latex-recommended exlive-bibtex-extra texlive-lang-german texlive-lang-english biber
sudo texhash
```

In VS Code, execute `ext install latex-workshop`. Simply open `thesis.tex`, open the "TeX" tab and press "compile".