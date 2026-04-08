
# 🚀 LexIntel™ v3.0 — Visual Lexical Intelligence System

![Version](https://img.shields.io/badge/Version-3.0_Visual_Edition-blue.svg)
![Python](https://img.shields.io/badge/Python-3.x-green.svg)
![C/Flex](https://img.shields.io/badge/Backend-C%20%7C%20FLEX-orange.svg)
![Complexity](https://img.shields.io/badge/Complexity-O\(N\)-critical.svg)


## 📖 Table of Contents

* [📌 Project Overview](#-project-overview)
* [💡 Motivation](#-motivation)
* [✨ Key Features](#-key-features)
* [🧠 System Architecture](#-system-architecture--complexity)
* [⚙️ Prerequisites & Installation](#️-prerequisites--installation)
* [🖥️ User Guide](#️-user-guide-modules)
* [📊 Performance & Complexity](#-performance--complexity)
* [🎯 Conclusion](#-conclusion)

---

## 📌 Project Overview

**LexIntel™ v3.0** is an advanced, enterprise-grade **Lexical Analysis Toolkit** and **Visual Tokenization System**.

It combines:

* ⚡ **High-performance C/FLEX backend**
* 🎨 **Modern Python GUI (CustomTkinter)**

Unlike traditional lexers that output plain text in terminals, LexIntel™ delivers a **real-time visual experience**, showing how text is processed, tokenized, and analyzed dynamically.

> 💡 Think of it as a **"Visual Compiler Frontend" + "Plagiarism Intelligence Engine"**

---

## 💡 Motivation

### ❌ Problem

* Traditional lexical analyzers:

  * Run in terminal
  * Provide no visualization
  * Hard to understand for beginners

### ✅ Solution

LexIntel™ introduces:

* Real-time token animation
* Visual classification of tokens
* Practical use-case (Plagiarism Detection)
* Modern UI/UX for better understanding

---

## ✨ Key Features

### 🔍 Live Visual Tokenizer (Plagiarism Engine)

* Compares **Document A vs Document B**
* Removes **Stop Words** (e.g., *is, am, the, and*)
* Calculates **Similarity Score**
* Real-time token animation:

  * 🟢 Matched Tokens
  * 🔴 Unmatched Tokens
  * ⚪ Ignored Tokens

---

### 🔠 Smart Format Normalizer

* Converts lowercase → uppercase using regex
* Preserves formatting
* Handles large files efficiently

---

### 🔄 High-Speed Content Refactor

* Optimized **Find & Replace engine**
* Works on full documents
* Extremely fast execution

---

### ⏱️ Live Analytics Dashboard

* Execution time (ms)
* Performance metrics
* Processing insights

---

### 💾 One-Click Export

* Save processed results instantly
* Output as `.txt` files

---

### 🎨 Premium UI/UX Design

* Clean, modern interface
* Light-blue professional theme
* Fully interactive dashboard

---

## 🧠 System Architecture & Complexity

LexIntel™ follows a **two-layer architecture**:

### 1️⃣ Frontend Layer (Python)

* Built using `customtkinter`
* Handles:

  * UI rendering
  * File input/output
  * Animation threads

---

### 2️⃣ Core Processing Engine (C + FLEX)

* Built using **Lex/FLEX**
* Implements **Deterministic Finite Automaton (DFA)**
* Handles:

  * Tokenization
  * Pattern matching
  * Text processing

---

### ⚡ Execution Flow

```
Input Text → FLEX Lexer → Token Stream → Python GUI → Visual Output
```

---

## 📊 Performance & Complexity

| Feature         | Complexity |
| --------------- | ---------- |
| Tokenization    | O(N)       |
| Text Processing | O(N)       |
| Refactor Engine | O(N)       |

> 🚀 Guaranteed linear time complexity regardless of file size

---

## ⚙️ Prerequisites & Installation

### 🔧 Requirements

* Python **3.8+**
* GCC Compiler (MinGW for Windows)
* FLEX (Fast Lexical Analyzer Generator)

---

### 📦 Step 1: Install Python Dependencies

```
pip install customtkinter
```

---

### ⚙️ Step 2: Run the Application

```
python main_gui.py
```

---

### 🛠️ Manual Compilation (If Needed)

If auto-compilation fails:

```
flex filename.l
gcc lex.yy.c -o output.exe
```

---

## 🖥️ User Guide (Modules)

---

### 🔍 1. Visual Plagiarism Analyzer

**Steps:**

1. Open *Visual Plagiarism* tab
2. Upload:

   * Base Document (Doc A)
   * Target Document (Doc B)
3. Click **RUN VISUAL TOKENIZER**

**Output:**

* Live token animation
* Similarity Score
* Verdict:

  * ✅ PASS (≥ 40%)
  * ❌ FAIL (< 40%)

---

### 🔠 2. Format Normalizer

**Steps:**

1. Open *Format Normalizer* tab
2. Upload `.txt` file
3. Click **Process Document**
4. Export result

---

### 🔄 3. Content Refactor

**Steps:**

1. Open *Content Refactor* tab
2. Upload file
3. Enter:

   * Find string
   * Replace string
4. Execute

**Output:**

* Updated document
* Execution time

---

## 🎯 Conclusion

LexIntel™ v3.0 is not just a lexer — it is a **complete visual lexical intelligence platform** that demonstrates:

* Compiler Design Concepts
* Real-Time Token Processing
* High-Performance Systems (C + FLEX)
* Modern UI Engineering
