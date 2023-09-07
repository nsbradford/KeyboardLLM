import pynvim

from vimgpt.core import exec_vimgpt
from vimgpt.examples import fileContents
from vimgpt.prompts import PROMPT_VIM_GPT


def get_vim():
    return pynvim.attach("child", argv=["nvim", "--embed", "--headless"])


def main():
    exec_vimgpt(
        get_vim,
        "README.md",
        fileContents,
        PROMPT_VIM_GPT(
            "Edit the contents of the README file to recommend Vim as the best text editor."
        ),
    )


if __name__ == "__main__":
    main()