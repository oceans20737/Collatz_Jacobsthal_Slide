# **Shiftless Collatz Model: J2 Interference and Slide Explorer**  

**Hiroshi Harada — August 1, 2026**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Document: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

## **概要（Overview）**

本プロジェクトは、Collatz写像における「$3n+1$」操作および「未知回数の2除算（シフト）」を、Jacobsthal（J）空間における **J波の隣接和（干渉）** と **基本波の加算（スライド）** として再定義する **Shiftless Model（シフトレス・モデル）** の計算・自動検証ツール群です。

従来の Collatz では、奇数 $n$ に対して $3n+1$ を行った後、**何回 2 で割られるか（シフト回数）が事前に予測できない** ことが最大の難所でした。

本モデルでは、奇数核の Jスピノル波に対して「隣接和」をとることで、次の奇数核の基盤となる **純粋なシフト流（$2^k$）** を抽出し、そこに階層に応じた **基本波（Least Significant Jacobsthal: LSJ）** を加算することで、算術的な割り算を一切行わずに軌道が推移する **Jスライド（J Slide）** を実現します。

これにより、Collatz軌道は「波の乗り換え（Wave Switching）」として幾何学的に理解でき、シフトの不確定性を完全に排除した **Shiftless Orbit（シフトレス軌道）** を構成できます。

---

## **ファイル構成（Files）**

### **code_01_collatz_j2_slide.py**
任意の奇数初期値から **シフトレス軌道（J Slide）** をシミュレートする Python スクリプト。

- **J2 Expansion**  
- **Marge（隣接和）**  
- **J2 Slide（基本波の加算）**  

の各ステップを計算し、**解析的な 2-adic Jacobsthal（J2）展開と完全一致するかを自動検証（Verification）** します。

結果はコンソール表示と、Excel互換の **CSV（TSV互換）形式** で出力されます。

---

### **REPORT_EN.pdf / REPORT_JP.pdf**
本理論の公式リサーチレポート（英語 / 日本語）。

- J波の構造  
- 隣接和（干渉）  
- 基本波の加算（スライド）  
- Shiftless Orbit の証明  
- 初期値 7 → 1 の完全展開例（Table 1）

などを含む、理論の中心文書です。

---

### **collatz_j2_slide_<初期値>.csv**
スクリプト実行によって自動生成されるデータファイル。

- 各階層（Level）ごとの波の推移  
- 垂直断面（Shiftless Orbit）  
- J2 Expansion / Marge / Slide の比較  

を確認できます。

---

## **使い方（Usage）**

Python 3.x 環境で以下を実行します：

```
python code_01_collatz_j2_slide.py
```

プロンプトが表示されたら、任意の正の奇数（例：7、11、17 など）を入力してください。

スクリプトは以下を自動計算します：

- **J2 Expansion**（奇数核のJ波展開）  
- **Marge**（隣接和によるシフト流抽出）  
- **J2 Slide**（基本波の加算による次核生成）  

さらに、各ステップで生成された J2 Slide 波が **解析的な J2スピノル展開と一致するか** を自動検証します。

---

## **自動検証機能（Verification）**

計算された J2 Slide波が、数学的恒等式に基づく「次の奇数核の本来の J2スピノル展開」と一致するかを判定します。

例：

```
--- Verification Result ---
[SUCCESS] 全ての J2 Slide が解析的J2波の展開と完全に一致しました。
```

すべて一致（SUCCESS）した場合、Collatz軌道が **算術的除算を一切含まない純粋な波の乗り換え現象（Wave Switching）** であることが数学的に証明されます。

---

## **ライセンス（License）**

- Research documents: **CC BY 4.0**  
- Python source code: **MIT License**

Copyright (c) 2026 Hiroshi Harada

---
