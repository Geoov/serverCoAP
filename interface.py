import logging
import Tkinter
import threading

class TextHandler(logging.Handler):
        def __init__(self, text):
        logging.Handler.__init__(self)
        self.text = text

    def emit(self, record):
        msg = self.format(record)
        def append():
            self.text.configure(state='normal')
            self.text.insert(Tkinter.END, msg + '\n')
            self.text.configure(state='disabled')
            self.text.yview(Tkinter.END)
        self.text.after(0, append)


if __name__ == '__main__':
    root = Tkinter.Tk()

    import ScrolledText
    st = ScrolledText.ScrolledText(root, state='disabled')
    st.configure(font='TkFixedFont')
    st.pack()

    text_handler = TextHandler(st)

    logger = logging.getLogger()
    logger.addHandler(text_handler)

    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')

    root.mainloop()
