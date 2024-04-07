'''
Main file for the specialized web crawler to identify potential leads for a sheet metal fabrication job shop factory focusing on users of Trumpf Machines.
'''
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from crawler import Crawler
from database import Database
class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Lead Generation Web Crawler")
        self.geometry("400x200")
        self.crawler = Crawler()
        self.database = Database()
        self.label = tk.Label(self, text="Select online platform to crawl:")
        self.label.pack()
        self.platform_var = tk.StringVar()
        self.platform_var.set("Platform 1")
        self.platform_dropdown = tk.OptionMenu(self, self.platform_var, "Platform 1", "Platform 2", "Platform 3")
        self.platform_dropdown.pack()
        self.start_button = tk.Button(self, text="Start Crawling", command=self.start_crawling)
        self.start_button.pack()
        self.export_button = tk.Button(self, text="Export Data", command=self.export_data)
        self.export_button.pack()
    def start_crawling(self):
        platform = self.platform_var.get()
        self.crawler.crawl(platform, self.database)
        messagebox.showinfo("Crawling Complete", "Crawling has been completed successfully.")
    def export_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files", "*.xlsx")])
        self.database.export_data(file_path)
        messagebox.showinfo("Export Complete", "Data has been exported successfully.")
if __name__ == "__main__":
    app = Application()
    app.mainloop()