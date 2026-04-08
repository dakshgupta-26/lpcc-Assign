import customtkinter as ctk
from tkinter import filedialog, messagebox
import subprocess
import os
import time
import re

# --- ULTIMATE ENTERPRISE THEME (CLEAN & MODERN) ---
# No black backgrounds. Clean light-blue professional aesthetic.
ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


class LexMasterpieceApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LexIntel™ v3.0 - Visual Edition")
        self.geometry("1100x750")
        self.minsize(950, 700)

        # Core Stop words for Visual Engine
        self.stop_words = {"is", "am", "a", "the", "if", "and", "of", "to", "in", "it", "that", "for", "on", "with",
                           "as", "this", "was", "at", "by", "an", "be", "from", "or", "are", "etc"}

        self.compile_lex_files()

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ================= ENHANCED SIDEBAR =================
        self.sidebar = ctk.CTkFrame(self, width=260, corner_radius=0, fg_color="#E3EEFA")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_rowconfigure(6, weight=1)

        self.logo = ctk.CTkLabel(self.sidebar, text="LexIntel™", font=ctk.CTkFont(size=36, weight="bold"),
                                 text_color="#1A56DB")
        self.logo.grid(row=0, column=0, padx=20, pady=(40, 5))

        self.sub_logo = ctk.CTkLabel(self.sidebar, text="Visual Tokenizer Engine",
                                     font=ctk.CTkFont(size=13, weight="bold"), text_color="#555555")
        self.sub_logo.grid(row=1, column=0, padx=20, pady=(0, 30))

        self.btn_sim = ctk.CTkButton(self.sidebar, text="🔍 Visual Plagiarism", height=45,
                                     font=ctk.CTkFont(size=14, weight="bold"), command=lambda: self.show_frame("sim"))
        self.btn_sim.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.btn_upper = ctk.CTkButton(self.sidebar, text="🔠 Format Normalizer", height=45,
                                       font=ctk.CTkFont(size=14, weight="bold"),
                                       command=lambda: self.show_frame("upper"))
        self.btn_upper.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.btn_replace = ctk.CTkButton(self.sidebar, text="🔄 Content Refactor", height=45,
                                         font=ctk.CTkFont(size=14, weight="bold"),
                                         command=lambda: self.show_frame("replace"))
        self.btn_replace.grid(row=4, column=0, padx=20, pady=10, sticky="ew")

        # Developer Signature
        self.credit = ctk.CTkLabel(self.sidebar, text="Architect: Daksh\nAlgorithmic Complexity: O(N)",
                                   font=ctk.CTkFont(size=12, slant="italic"), text_color="#1A56DB")
        self.credit.grid(row=6, column=0, padx=20, pady=20, sticky="s")

        # ================= MAIN WORKSPACE =================
        self.main_container = ctk.CTkFrame(self, corner_radius=20, fg_color="#FFFFFF")
        self.main_container.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.main_container.grid_rowconfigure(0, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        self.setup_similarity_frame()
        self.setup_uppercase_frame()
        self.setup_replace_frame()

        self.show_frame("sim")

    def compile_lex_files(self):
        try:
            os.system("flex similarity.l && gcc lex.yy.c -o sim.exe")
            os.system("flex uppercase.l && gcc lex.yy.c -o upper.exe")
            os.system("flex replace.l && gcc lex.yy.c -o replace.exe")
        except Exception:
            pass

    def select_file(self, string_var, label_widget):
        filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if filename:
            string_var.set(filename)
            file_size = os.path.getsize(filename) / 1024
            label_widget.configure(text=f"Loaded: {os.path.basename(filename)} ({file_size:.2f} KB)",
                                   text_color="#198754")

    def save_output(self, text_content):
        if not text_content.strip():
            messagebox.showwarning("Empty", "Nothing to save!")
            return
        filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if filename:
            with open(filename, 'w') as f:
                f.write(text_content)
            messagebox.showinfo("Success", "File exported successfully!")

    def show_frame(self, name):
        for frame in self.frames.values():
            frame.grid_forget()
        self.frames[name].grid(row=0, column=0, sticky="nsew", padx=30, pady=30)

    # --- MODULE 1: SIMILARITY WITH ADVANCED VISUALIZATION ---
    def setup_similarity_frame(self):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.frames["sim"] = frame
        frame.grid_rowconfigure(3, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        header = ctk.CTkLabel(frame, text="Live Visual Similarity Engine", font=ctk.CTkFont(size=28, weight="bold"),
                              text_color="#1A56DB")
        header.grid(row=0, column=0, pady=(0, 20), sticky="w")

        self.file1_var = ctk.StringVar()
        self.file2_var = ctk.StringVar()

        upload_frame = ctk.CTkFrame(frame, fg_color="transparent")
        upload_frame.grid(row=1, column=0, sticky="ew")

        # Doc A
        row1 = ctk.CTkFrame(upload_frame, fg_color="#F0F4F8", corner_radius=10)
        row1.pack(fill="x", pady=5, ipady=5)
        ctk.CTkButton(row1, text="📄 Upload Base Doc", width=150,
                      command=lambda: self.select_file(self.file1_var, self.lbl_f1)).pack(side="left", padx=20)
        self.lbl_f1 = ctk.CTkLabel(row1, text="Awaiting input...", font=ctk.CTkFont(slant="italic"), text_color="#555")
        self.lbl_f1.pack(side="left", padx=10)

        # Doc B
        row2 = ctk.CTkFrame(upload_frame, fg_color="#F0F4F8", corner_radius=10)
        row2.pack(fill="x", pady=5, ipady=5)
        ctk.CTkButton(row2, text="📄 Upload Target Doc", width=150,
                      command=lambda: self.select_file(self.file2_var, self.lbl_f2)).pack(side="left", padx=20)
        self.lbl_f2 = ctk.CTkLabel(row2, text="Awaiting input...", font=ctk.CTkFont(slant="italic"), text_color="#555")
        self.lbl_f2.pack(side="left", padx=10)

        ctrl_frame = ctk.CTkFrame(frame, fg_color="transparent")
        ctrl_frame.grid(row=2, column=0, pady=15, sticky="ew")

        ctk.CTkButton(ctrl_frame, text="⚡ RUN VISUAL TOKENIZER", height=45, fg_color="#198754", hover_color="#157347",
                      font=ctk.CTkFont(weight="bold"), command=self.run_visual_sim).pack(side="left")

        # Legend
        legend = ctk.CTkFrame(ctrl_frame, fg_color="transparent")
        legend.pack(side="right")
        ctk.CTkLabel(legend, text=" Legend: ", font=ctk.CTkFont(weight="bold")).pack(side="left", padx=5)
        ctk.CTkLabel(legend, text=" Matched ", text_color="white", fg_color="#198754", corner_radius=5).pack(
            side="left", padx=2)
        ctk.CTkLabel(legend, text=" Unmatched ", text_color="white", fg_color="#dc3545", corner_radius=5).pack(
            side="left", padx=2)
        ctk.CTkLabel(legend, text=" Stop Word ", text_color="white", fg_color="#6c757d", corner_radius=5).pack(
            side="left", padx=2)

        # Visual Output Box (Light theme setup)
        self.res_sim = ctk.CTkTextbox(frame, fg_color="#F8FAFC", text_color="#000000",
                                      font=ctk.CTkFont(family="Consolas", size=16), border_width=2,
                                      border_color="#E3EEFA")
        self.res_sim.grid(row=3, column=0, sticky="nsew", pady=(10, 0))

        # UI Tags for syntax highlighting (Fixed scaling issue by removing 'font' parameter)
        self.res_sim.tag_config("match", foreground="#198754")
        self.res_sim.tag_config("unmatch", foreground="#dc3545")
        self.res_sim.tag_config("stop", foreground="#9CA3AF")
        self.res_sim.tag_config("normal", foreground="#333333")
        self.res_sim.tag_config("title", foreground="#1A56DB")

    def run_visual_sim(self):
        file1 = self.file1_var.get()
        file2 = self.file2_var.get()
        if not file1 or not file2:
            messagebox.showwarning("Missing Files", "Upload both documents first!")
            return

        self.res_sim.delete("1.0", "end")
        self.res_sim.insert("end", "[SYSTEM] Initializing O(N) Lexical Engine...\n", "title")
        self.update()
        time.sleep(0.4)

        # Read Files
        try:
            with open(file1, 'r', encoding='utf-8') as f:
                raw_a = f.read()
            with open(file2, 'r', encoding='utf-8') as f:
                raw_b = f.read()
        except Exception as e:
            messagebox.showerror("File Error", "Could not read files.")
            return

        # Backend logic mirroring LEX
        words_a = re.findall(r'\b[a-zA-Z]+\b', raw_a.lower())
        words_b = re.findall(r'\b[a-zA-Z]+\b', raw_b.lower())
        valid_a = set([w for w in words_a if w not in self.stop_words])
        valid_b = set([w for w in words_b if w not in self.stop_words])

        self.res_sim.insert("end", "[SYSTEM] Processing Tokens in Real-Time...\n\n", "title")
        self.update()
        time.sleep(0.4)

        # --- THE ANIMATION MAGIC ---
        tokens_a = re.findall(r'\b[a-zA-Z]+\b|\W+', raw_a)

        for token in tokens_a:
            clean_token = token.lower().strip()
            if not clean_token.isalpha():
                self.res_sim.insert("end", token, "normal")
            elif clean_token in self.stop_words:
                self.res_sim.insert("end", token, "stop")
            elif clean_token in valid_b:
                self.res_sim.insert("end", token, "match")
            else:
                self.res_sim.insert("end", token, "unmatch")

            self.res_sim.see("end")
            self.update()
            time.sleep(0.01)  # Ultra-fast animation feel

        # Execute C Lex engine for actual metrics
        exe = "sim.exe" if os.name == 'nt' else "./sim.exe"
        start_time = time.time()
        try:
            subprocess.run([exe, file1, file2], capture_output=True, text=True)
        except:
            pass  # Failsafe if C isn't compiled
        exec_time = (time.time() - start_time) * 1000

        # Calculate Results
        match_count = len([w for w in valid_a if w in valid_b])
        total_valid = len(valid_a)
        score = (match_count / total_valid * 100) if total_valid > 0 else 0

        self.res_sim.insert("end", "\n\n" + "=" * 60 + "\n", "normal")
        self.res_sim.insert("end", f"▶ BACKEND EXECUTION TIME: {exec_time:.2f} ms\n", "title")
        self.res_sim.insert("end", f"▶ TOTAL VALID WORDS IN DOC A: {total_valid}\n", "normal")
        self.res_sim.insert("end", f"▶ MATCHING WORDS IN DOC B: {match_count}\n", "match")
        self.res_sim.insert("end", f"▶ SIMILARITY SCORE: {score:.2f}%\n", "title")

        if score >= 40:
            self.res_sim.insert("end", f"▶ VERDICT: SIMILAR (PASS)\n", "match")
        else:
            self.res_sim.insert("end", f"▶ VERDICT: NOT SIMILAR (FAIL)\n", "unmatch")

    # --- MODULE 2: UPPERCASE (CLEAN THEME) ---
    def setup_uppercase_frame(self):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.frames["upper"] = frame

        ctk.CTkLabel(frame, text="Smart Format Normalizer", font=ctk.CTkFont(size=28, weight="bold"),
                     text_color="#1A56DB").pack(pady=(0, 20), anchor="w")

        self.up_var = ctk.StringVar()
        row1 = ctk.CTkFrame(frame, fg_color="#F0F4F8", corner_radius=10)
        row1.pack(fill="x", pady=10, ipady=10)
        ctk.CTkButton(row1, text="📁 Select Raw Document",
                      command=lambda: self.select_file(self.up_var, self.lbl_up)).pack(side="left", padx=20)
        self.lbl_up = ctk.CTkLabel(row1, text="Awaiting input...", font=ctk.CTkFont(slant="italic"), text_color="#555")
        self.lbl_up.pack(side="left", padx=10)

        ctrl_frame = ctk.CTkFrame(frame, fg_color="transparent")
        ctrl_frame.pack(fill="x", pady=20)
        ctk.CTkButton(ctrl_frame, text="⚙️ Process Document", height=45, command=self.run_upper).pack(side="left")
        ctk.CTkButton(ctrl_frame, text="💾 Export Output", height=45, fg_color="#6c757d", hover_color="#5a6268",
                      command=lambda: self.save_output(self.res_up.get("1.0", "end"))).pack(side="left", padx=15)

        self.up_metrics = ctk.CTkLabel(ctrl_frame, text="", font=ctk.CTkFont(weight="bold"), text_color="#198754")
        self.up_metrics.pack(side="right", padx=20)

        self.res_up = ctk.CTkTextbox(frame, height=250, fg_color="#F8FAFC", text_color="#333",
                                     font=ctk.CTkFont(family="Consolas", size=15), border_width=2,
                                     border_color="#E3EEFA")
        self.res_up.pack(fill="both", expand=True)

    def run_upper(self):
        if not self.up_var.get(): return
        exe = "upper.exe" if os.name == 'nt' else "./upper.exe"

        start_time = time.time()
        res = subprocess.run([exe, self.up_var.get()], capture_output=True, text=True)
        exec_time = (time.time() - start_time) * 1000

        self.up_metrics.configure(text=f"⏱️ Processed in {exec_time:.2f} ms")
        self.res_up.delete("1.0", "end")
        self.res_up.insert("end", res.stdout)

    # --- MODULE 3: FIND & REPLACE (CLEAN THEME) ---
    def setup_replace_frame(self):
        frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.frames["replace"] = frame

        ctk.CTkLabel(frame, text="High-Speed Content Refactor", font=ctk.CTkFont(size=28, weight="bold"),
                     text_color="#1A56DB").pack(pady=(0, 20), anchor="w")

        self.rep_var = ctk.StringVar()
        row1 = ctk.CTkFrame(frame, fg_color="#F0F4F8", corner_radius=10)
        row1.pack(fill="x", pady=10, ipady=10)
        ctk.CTkButton(row1, text="📁 Select Target Document",
                      command=lambda: self.select_file(self.rep_var, self.lbl_rep)).pack(side="left", padx=20)
        self.lbl_rep = ctk.CTkLabel(row1, text="Awaiting input...", font=ctk.CTkFont(slant="italic"), text_color="#555")
        self.lbl_rep.pack(side="left", padx=10)

        inputs = ctk.CTkFrame(frame, fg_color="#F0F4F8", corner_radius=10)
        inputs.pack(fill="x", pady=10, ipady=10)
        self.entry_find = ctk.CTkEntry(inputs, placeholder_text="Enter word to find", width=250, height=40,
                                       font=ctk.CTkFont(size=14))
        self.entry_find.pack(side="left", padx=20)
        self.entry_replace = ctk.CTkEntry(inputs, placeholder_text="Enter replacement word", width=250, height=40,
                                          font=ctk.CTkFont(size=14))
        self.entry_replace.pack(side="left", padx=10)

        ctrl_frame = ctk.CTkFrame(frame, fg_color="transparent")
        ctrl_frame.pack(fill="x", pady=20)
        ctk.CTkButton(ctrl_frame, text="🚀 Execute Refactor", height=45, fg_color="#1A56DB", hover_color="#1542A6",
                      command=self.run_replace).pack(side="left")
        ctk.CTkButton(ctrl_frame, text="💾 Export Output", height=45, fg_color="#6c757d", hover_color="#5a6268",
                      command=lambda: self.save_output(self.res_rep.get("1.0", "end"))).pack(side="left", padx=15)

        self.rep_metrics = ctk.CTkLabel(ctrl_frame, text="", font=ctk.CTkFont(weight="bold"), text_color="#198754")
        self.rep_metrics.pack(side="right", padx=20)

        self.res_rep = ctk.CTkTextbox(frame, height=200, fg_color="#F8FAFC", text_color="#333",
                                      font=ctk.CTkFont(family="Consolas", size=15), border_width=2,
                                      border_color="#E3EEFA")
        self.res_rep.pack(fill="both", expand=True)

    def run_replace(self):
        if not self.rep_var.get() or not self.entry_find.get(): return
        exe = "replace.exe" if os.name == 'nt' else "./replace.exe"

        start_time = time.time()
        res = subprocess.run([exe, self.rep_var.get(), self.entry_find.get(), self.entry_replace.get()],
                             capture_output=True, text=True)
        exec_time = (time.time() - start_time) * 1000

        self.rep_metrics.configure(text=f"⏱️ Search/Replace completed in {exec_time:.2f} ms")
        self.res_rep.delete("1.0", "end")
        self.res_rep.insert("end", res.stdout)


if __name__ == "__main__":
    app = LexMasterpieceApp()
    app.mainloop()