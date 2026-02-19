import tkinter as tk
from tkinter import messagebox
import requests
import webbrowser

def open_link(url):
    webbrowser.open_new_tab(url)

def fetch_news():
    query = topic_entry.get().strip()
    if not query:
        messagebox.showwarning("Input Error", "Please enter a topic to search.")
        return

    api_key = "b27f41ab72e54809b7d21f2dffe68978"
    url = f"https://newsapi.org/v2/everything?q={query}&from=2025-10-06&sortBy=publishedAt&apiKey={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        if data.get("status") != "ok":
            messagebox.showerror("Error", f"Failed to fetch news: {data.get('message')}")
            return

        articles = data.get("articles", [])

        # clear old content
        for widget in scrollable_frame.winfo_children():
            widget.destroy()

        if not articles:
            tk.Label(scrollable_frame, text="No news found for this topic.", font=("Helvetica", 12),
                     fg="red", bg="#f2f2f2").pack(pady=10)
            return

        for i, article in enumerate(articles[:10]):
            title = article.get("title", "No title")
            url = article.get("url", "")

            # Create a container frame for each article
            article_frame = tk.Frame(scrollable_frame, bg="white", bd=1, relief="solid")
            article_frame.pack(fill="x", padx=10, pady=5)

            tk.Label(article_frame, text=f"{i+1}. {title}", font=("Helvetica", 12, "bold"),
                     bg="white", wraplength=650, justify="left").pack(anchor="w", padx=10, pady=5)

            if url:
                tk.Button(article_frame, text="🔗 Open Article", font=("Helvetica", 10, "bold"),
                          bg="#0078D7", fg="white", cursor="hand2",
                          command=lambda link=url: open_link(link)).pack(anchor="e", padx=10, pady=5)
            else:
                tk.Label(article_frame, text="No URL available", font=("Helvetica", 10, "italic"),
                         bg="white", fg="gray").pack(anchor="e", padx=10, pady=5)

        # update scroll region
        canvas.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred:\n{e}")

# ---------- UI ----------
root = tk.Tk()
root.title("🗞️ News Reader")
root.geometry("750x600")
root.config(bg="#f2f2f2")

# Title
tk.Label(root, text="📰 News Reader App", font=("Helvetica", 20, "bold"),
         bg="#f2f2f2", fg="#333").pack(pady=10)

# Search section
search_frame = tk.Frame(root, bg="#f2f2f2")
search_frame.pack(pady=10)

tk.Label(search_frame, text="Enter Topic:", font=("Helvetica", 12),
         bg="#f2f2f2").grid(row=0, column=0, padx=5)
topic_entry = tk.Entry(search_frame, font=("Helvetica", 12), width=30)
topic_entry.grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="🔍 Search", font=("Helvetica", 12, "bold"),
          bg="#4CAF50", fg="white", command=fetch_news).grid(row=0, column=2, padx=5)

# Canvas + Scrollbar
frame_container = tk.Frame(root)
frame_container.pack(fill="both", expand=True, padx=10, pady=10)

canvas = tk.Canvas(frame_container, bg="#f2f2f2", highlightthickness=0)
scrollbar = tk.Scrollbar(frame_container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")
canvas.pack(side="left", fill="both", expand=True)

scrollable_frame = tk.Frame(canvas, bg="#f2f2f2")
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

canvas.configure(yscrollcommand=scrollbar.set)

# enable mousewheel scrolling
def _on_mousewheel(event):
    canvas.yview_scroll(int(-1*(event.delta/120)), "units")

canvas.bind_all("<MouseWheel>", _on_mousewheel)

# Footer
tk.Label(root, text="Powered by NewsAPI.org", font=("Helvetica", 10),
         bg="#f2f2f2", fg="#666").pack(side=tk.BOTTOM, pady=5)

root.mainloop()
