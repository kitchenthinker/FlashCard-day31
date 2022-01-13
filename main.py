# IMPORT
import tkinter
import pandas
import json
import time
import random

# CONST
BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

# VARIABLES
current_card = None
main_func = None
file_path_learn = "./data/words_2_learn.csv"
file_path_start_pack = "./data/french_words.csv"
# FUNCTIONALITY


def pick_next_card():
    global current_card, main_func
    main_window.after_cancel(main_func)
    current_card = random.choice(dict_for_work)
    canvas_cover.itemconfig(canvas_img, image=img_card_front)
    canvas_cover.itemconfig(canvas_text_language, fill="black", text="French")
    canvas_cover.itemconfig(canvas_text_word, fill="black", text=current_card["French"])
    main_func = main_window.after(3000, func=flip_up_card)


def wrong_button():
    pick_next_card()
    #


def right_button():
    global current_card
    dict_for_work.remove(current_card)
    update_file = pandas.DataFrame(dict_for_work).to_csv(file_path_learn, index=False)
    pick_next_card()
    #


def flip_up_card():
    global main_func, current_card
    if current_card is not None:
        canvas_cover.itemconfig(canvas_img, image=img_card_back)
        canvas_cover.itemconfig(canvas_text_language, fill="white", text="English")
        canvas_cover.itemconfig(canvas_text_word, fill="white", text=current_card["English"])


main_window = tkinter.Tk()
main_window.title("FLASH CARDS")
main_window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, width=800, height=526, )
img_card_back = tkinter.PhotoImage(file="./images/card_back.png")
img_card_front = tkinter.PhotoImage(file="./images/card_front.png")
img_right = tkinter.PhotoImage(file="./images/right.png")
img_wrong = tkinter.PhotoImage(file="./images/wrong.png")

canvas_cover = tkinter.Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_img = canvas_cover.create_image(400, 263, image=img_card_front)

canvas_text_language = canvas_cover.create_text(400, 150, text="test", font=(FONT_NAME, 40, "italic"))
canvas_text_word = canvas_cover.create_text(400, 263, text="test", font=(FONT_NAME, 60, "bold"))
canvas_cover.grid(row=0, column=0, columnspan=2)

canvas_btn_right = tkinter.Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=img_right, command=right_button)
canvas_btn_wrong = tkinter.Button(bg=BACKGROUND_COLOR, highlightthickness=0, image=img_wrong, command=wrong_button)

canvas_btn_wrong.grid(row=1, column=0)
canvas_btn_right.grid(row=1, column=1)


def return_dictionary():
    dictionary_words = None
    try:
        with open(file_path_learn) as file_words:
            pass
    except FileNotFoundError:
        dictionary_words = pandas.read_csv(file_path_start_pack)
        dictionary_words.to_csv(file_path_learn, index=False)
    finally:
        dictionary_words = pandas.read_csv(file_path_learn)
        return dictionary_words.to_dict("records")


dict_for_work = return_dictionary()
main_func = main_window.after(3000, func=flip_up_card)
pick_next_card()
main_window.mainloop()
