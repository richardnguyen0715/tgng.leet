# Dynamic Programming là gì?

Nếu phải giải thích Dynamic Programming (DP) bằng **một câu duy nhất**, mình sẽ nói:

> **Dynamic Programming là cách giải một bài toán bằng cách chia nó thành các bài toán con nhỏ hơn, lưu lại kết quả của các bài toán con đó, rồi sử dụng lại chúng để xây dựng lời giải lớn hơn.**

Nhưng câu này **chưa đủ** để hiểu DP.

Điểm quan trọng nhất của DP không phải là "có một mảng `dp`", cũng không phải là "có công thức `dp[i]`".

**Triết lý thật sự của DP là:**

> **Một bài toán lớn có thể được mô tả hoàn toàn bằng một số lượng hữu hạn các trạng thái nhỏ hơn, và mỗi trạng thái chỉ cần biết thông tin cần thiết từ các trạng thái trước đó để quyết định đáp án của nó.**

Đây chính là thứ chúng ta cần đào sâu.

---

# 1. Trước tiên: tại sao chúng ta cần Dynamic Programming?

Hãy bắt đầu bằng một bài rất đơn giản:

**Climbing Stairs**

Bạn có `n` bậc thang.

Mỗi lần có thể đi:

* 1 bước
* hoặc 2 bước

Hỏi có bao nhiêu cách để lên đến bậc `n`?

Ví dụ:

```text
n = 1 → 1 cách

n = 2 → 2 cách
        1 + 1
        2

n = 3 → 3 cách
        1 + 1 + 1
        1 + 2
        2 + 1
```

Đến đây chúng ta có thể nhận ra:

Để đến bậc `n`, bước cuối cùng phải là:

```text
đến n-1 rồi bước 1
```

hoặc:

```text
đến n-2 rồi bước 2
```

Do đó:

```text
ways(n) = ways(n-1) + ways(n-2)
```

Đây chính là Fibonacci.

---

# 2. Nhưng Fibonacci đệ quy có vấn đề gì?

Ta có thể viết:

```python
def fib(n):
    if n <= 1:
        return n

    return fib(n - 1) + fib(n - 2)
```

Nhìn rất đẹp.

Nhưng hãy nhìn cây đệ quy:

```text
                    fib(5)
                  /        \
             fib(4)        fib(3)
             /   \          /   \
         fib(3) fib(2)   fib(2) fib(1)
         /  \
      fib(2) fib(1)
```

Bạn thấy vấn đề chưa?

`fib(3)` được tính nhiều lần.

`fib(2)` còn bị tính **rất nhiều lần**.

Ví dụ:

```text
fib(5)
 ├── fib(4)
 │    ├── fib(3)
 │    │    ├── fib(2)
 │    │    └── fib(1)
 │    └── fib(2)
 │
 └── fib(3)
      ├── fib(2)
      └── fib(1)
```

Chúng ta đang giải đi giải lại **cùng một bài toán con**.

Đây là một trong những dấu hiệu quan trọng nhất của DP.

---

# 3. Hai đặc điểm cốt lõi của Dynamic Programming

Một bài toán thường phù hợp với DP khi có:

## 3.1. Overlapping Subproblems

Các bài toán con **bị lặp lại**.

Ví dụ:

```text
fib(5)
```

cần:

```text
fib(4)
fib(3)
```

`fib(4)` lại cần:

```text
fib(3)
fib(2)
```

Vậy `fib(3)` xuất hiện nhiều lần.

Thay vì tính:

```text
fib(3)
fib(3)
fib(3)
fib(3)
...
```

ta chỉ tính một lần:

```text
fib(3) = 2
```

sau đó lưu lại.

Đây gọi là **memoization**.

---

# 4. Memoization

Ta có thể sửa:

```python
memo = {}

def fib(n):
    if n <= 1:
        return n

    if n in memo:
        return memo[n]

    memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]
```

Lần đầu:

```text
fib(3)
```

được tính.

Sau đó lưu:

```text
memo[3] = 2
```

Nếu lần sau cần `fib(3)`:

```text
if n in memo:
    return memo[n]
```

Không cần tính lại.

---

# 5. Đây chính là một dạng Dynamic Programming

Có hai cách triển khai DP phổ biến:

### Top-down

```text
Recursion
+
Memoization
```

### Bottom-up

```text
Tính từ nhỏ → lớn
```

Ví dụ bottom-up:

```python
dp = [0] * (n + 1)

dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1] + dp[i - 2]
```

Cả hai đều dựa trên **cùng một ý tưởng toán học**.

Đây là điều rất quan trọng:

> **Memoization và Tabulation không phải là hai loại DP khác nhau về bản chất. Chúng chỉ là hai cách thực thi cùng một recurrence/state transition.**

---

# 6. Nhưng "bài toán con bị lặp" vẫn chưa đủ

Đây là phần rất quan trọng.

Một bài toán DP thường còn có tính chất thứ hai:

## Optimal Substructure

Hiểu đơn giản:

> **Lời giải tối ưu của bài toán lớn có thể được xây dựng từ lời giải tối ưu của các bài toán con.**

Ví dụ kinh điển:

**House Robber**

Bạn có:

```text
[2, 7, 9, 3, 1]
```

Không được lấy hai nhà cạnh nhau.

Muốn biết số tiền lớn nhất có thể lấy.

Tại nhà `i`, có hai lựa chọn:

```text
Không lấy i
```

hoặc:

```text
Lấy i
```

Nếu lấy `i`, bạn không thể lấy `i-1`.

Vậy:

```text
dp[i] = max(
    dp[i-1],
    dp[i-2] + nums[i]
)
```

Tại sao công thức này đúng?

Bởi vì nếu quyết định **lấy nhà i**, phần còn lại tốt nhất phải là:

```text
lời giải tốt nhất của 0..i-2
```

Nếu không thì chúng ta có thể thay nó bằng một lời giải tốt hơn.

Đây chính là **optimal substructure**.

---

# 7. Đây là "linh hồn" của DP

Có thể hình dung:

```text
                 BÀI TOÁN LỚN
                      |
             chia thành state
                      |
        ┌─────────────┴─────────────┐
        ↓                           ↓
   bài toán con A              bài toán con B
        ↓                           ↓
    giải A                       giải B
        └─────────────┬─────────────┘
                      ↓
                 kết hợp lại
                      ↓
                lời giải lớn
```

Nhưng để làm được điều đó, chúng ta phải trả lời một câu hỏi cực kỳ quan trọng:

> **"Tôi cần lưu lại thông tin gì để mô tả hoàn toàn một bài toán con?"**

Đây chính là **state**.

---

# 8. DP State là gì?

Đây có lẽ là khái niệm **quan trọng nhất** khi học DP.

Ví dụ:

```text
dp[i]
```

không đơn giản chỉ là "một biến".

Nó phải có một ý nghĩa rõ ràng.

Ví dụ:

```text
dp[i] = số cách để đi tới bậc i
```

hoặc:

```text
dp[i] = số tiền lớn nhất có thể lấy từ 0..i
```

hoặc:

```text
dp[i] = độ dài LIS kết thúc tại i
```

hoặc:

```text
dp[i][j] = LCS của s1[0..i] và s2[0..j]
```

Điều quan trọng là:

> **Mỗi state phải đại diện cho một bài toán con cụ thể.**

---

# 9. Sai state → cả bài DP sai

Đây là lý do rất nhiều người học DP cảm thấy:

> "Tại sao DP khó thế?"

Thường không phải vì code khó.

Mà vì họ **không biết `dp[i]` nên đại diện cho cái gì**.

Ví dụ bài:

```text
Longest Increasing Subsequence
```

Sai lầm phổ biến là nghĩ:

```text
dp[i] = LIS của toàn bộ array từ 0 tới i
```

Đây không phải state thuận tiện nhất.

Thay vào đó:

```text
dp[i] = độ dài LIS kết thúc tại i
```

Bây giờ ta có thể chuyển trạng thái:

```text
dp[i] = max(dp[j] + 1)
```

với:

```text
j < i
nums[j] < nums[i]
```

Đây là một state tốt vì nó chứa đúng thông tin cần thiết để xây dựng state tiếp theo.

---

# 10. "State" phải chứa đủ thông tin

Đây là một nguyên lý cực kỳ quan trọng:

> **State phải chứa đủ thông tin để quyết định tương lai, nhưng không nên chứa thông tin dư thừa.**

Hãy tưởng tượng bạn đang chơi một game.

Bạn đang đứng ở vị trí:

```text
x = 5
```

Nhưng để quyết định bước tiếp theo, bạn còn cần biết:

```text
máu còn bao nhiêu
```

Nếu chỉ lưu:

```text
dp[5]
```

thì chưa đủ.

Có thể phải lưu:

```text
dp[position][health]
```

Tương tự, trong các bài:

```text
dp[i][j]
dp[i][j][k]
```

các chiều bổ sung tồn tại vì **chúng ta cần thêm thông tin để xác định trạng thái**.

---

# 11. Ví dụ cực kỳ quan trọng: 2D DP

Xét:

**Longest Common Subsequence**

```text
s1 = "abcde"
s2 = "ace"
```

Ta định nghĩa:

```text
dp[i][j]
```

là:

> LCS của `s1[0..i]` và `s2[0..j]`.

Bây giờ xét hai ký tự cuối.

Nếu:

```text
s1[i] == s2[j]
```

thì:

```text
dp[i][j] = dp[i-1][j-1] + 1
```

Nếu khác:

```text
dp[i][j] = max(
    dp[i-1][j],
    dp[i][j-1]
)
```

Bạn có thể thấy một pattern:

```text
State
 ↓
Choices
 ↓
Transition
 ↓
Base case
 ↓
Answer
```

Đây chính là skeleton của rất nhiều bài DP.

---

# 12. Vậy "Dynamic" trong Dynamic Programming nghĩa là gì?

Tên gọi này đôi khi gây hiểu nhầm.

Nó **không có nghĩa đơn giản là "chương trình chạy động"**.

Trong bối cảnh DP, ý tưởng là bài toán được xem như một hệ thống có các **trạng thái**, và ta tiến triển giữa các trạng thái đó.

Ví dụ:

```text
state 0
   ↓
state 1
   ↓
state 2
   ↓
state 3
   ↓
...
```

Mỗi state chứa kết quả của một bài toán con.

---

# 13. Một cách nhìn sâu hơn: DP là Graph trên các State

Đây là một góc nhìn rất mạnh.

Hãy coi mỗi state là một **node**.

Ví dụ Fibonacci:

```text
0
1
2
3
4
5
```

Có các dependency:

```text
5 → 4
5 → 3

4 → 3
4 → 2

3 → 2
3 → 1
```

Thực tế đây là một **DAG** (Directed Acyclic Graph).

DP chính là:

> **Tính giá trị trên các node của một DAG theo thứ tự dependency, đồng thời tránh tính một node nhiều lần.**

Điều này giải thích tại sao DP và graph có mối quan hệ rất sâu.

---

# 14. Từ đây ta có một định nghĩa mạnh hơn

Bạn có thể hiểu Dynamic Programming như sau:

> **DP là quá trình tính toán trên một không gian trạng thái, trong đó mỗi trạng thái được biểu diễn bởi một số tham số, trạng thái mới được suy ra từ các trạng thái đã biết thông qua transition, và kết quả của mỗi trạng thái được lưu lại để tránh tính toán lặp.**

Đây là định nghĩa mình muốn bạn nhớ.

---

# 15. Triết lý để xây dựng một thuật toán DP hoàn chỉnh

Bây giờ đến phần quan trọng nhất trong câu hỏi của bạn.

Khi gặp **bất kỳ bài toán DP nào**, hãy đi theo pipeline này:

```text
                BÀI TOÁN
                   │
                   ▼
          1. Xác định trạng thái
                   │
                   ▼
          2. Xác định state meaning
                   │
                   ▼
          3. Xác định các lựa chọn
                   │
                   ▼
          4. Viết transition
                   │
                   ▼
          5. Xác định base cases
                   │
                   ▼
          6. Xác định thứ tự tính
                   │
                   ▼
          7. Xác định answer
                   │
                   ▼
          8. Tối ưu memory nếu cần
```

Hãy đi từng bước.

---

# 16. Bước 1 — Xác định "state"

Đây là bước khó nhất.

Hỏi:

> **Một bài toán con được xác định bởi những thông tin nào?**

Ví dụ:

### Climbing Stairs

Chỉ cần biết:

```text
đang ở bậc i
```

→

```text
dp[i]
```

### LCS

Cần biết:

```text
đang xét tới i của string A
đang xét tới j của string B
```

→

```text
dp[i][j]
```

### Knapsack

Cần biết:

```text
đang xét item i
capacity còn lại là j
```

→

```text
dp[i][j]
```

### Stock

Có thể cần:

```text
day
holding / not holding
number of transactions
```

→

```text
dp[day][holding][transactions]
```

Mỗi chiều tồn tại vì nó đại diện cho **một phần thông tin của state**.

---

# 17. Bước 2 — Định nghĩa state bằng một câu

Đừng code ngay.

Hãy viết một câu tiếng Việt.

Ví dụ:

```text
dp[i] = số cách để đến bậc i
```

hoặc:

```text
dp[i] = lợi nhuận lớn nhất có thể đạt được trong i ngày đầu tiên
```

hoặc:

```text
dp[i][j] = LCS của hai prefix s1[0..i-1] và s2[0..j-1]
```

Nếu bạn **không thể nói rõ `dp[i][j]` nghĩa là gì bằng một câu**, thì chưa nên viết code.

Đây là một nguyên tắc mình rất khuyên bạn áp dụng.

---

# 18. Bước 3 — Xác định lựa chọn

Hỏi:

> **Ở state hiện tại, tôi có những lựa chọn nào?**

Ví dụ House Robber:

```text
Nhà i
├── không lấy
└── lấy
```

Knapsack:

```text
Item i
├── không chọn
└── chọn
```

LCS:

```text
s1[i], s2[j]
├── giống nhau → lấy cả hai
└── khác nhau → bỏ một phía
```

Stock:

```text
Ngày i
├── buy
├── sell
└── hold
```

Đây thường là bước giúp bạn tìm ra transition.

---

# 19. Bước 4 — Viết Transition

Transition là:

> **Từ những state nào tôi có thể đi tới state hiện tại?**

Ví dụ:

```text
dp[i]
```

có thể đến từ:

```text
dp[i-1]
dp[i-2]
```

nên:

```text
dp[i] = ...
```

Trong LCS:

```text
dp[i][j]
```

đến từ:

```text
dp[i-1][j]
dp[i][j-1]
dp[i-1][j-1]
```

Trong Knapsack:

```text
dp[i][capacity]
```

có thể đến từ:

```text
dp[i-1][capacity]
dp[i-1][capacity-weight]
```

Đây chính là **transition relation**.

---

# 20. Bước 5 — Base Case

Đây là nơi nhiều người mắc lỗi.

Hỏi:

> **State nhỏ nhất có ý nghĩa gì?**

Ví dụ Fibonacci:

```text
dp[0] = 0
dp[1] = 1
```

Unique Paths:

```text
dp[0][0] = 1
```

LCS:

```text
dp[0][j] = 0
dp[i][0] = 0
```

Knapsack:

```text
0 items → answer = 0
```

Base case không phải phần phụ.

Nó là **điểm bắt đầu của toàn bộ hệ thống recurrence**.

---

# 21. Bước 6 — Xác định thứ tự tính

Nếu:

```text
dp[i]
```

phụ thuộc:

```text
dp[i-1]
dp[i-2]
```

thì phải tính:

```text
0
1
2
3
4
...
```

Nếu:

```text
dp[i][j]
```

phụ thuộc:

```text
dp[i-1][j]
dp[i][j-1]
```

thì thường đi:

```text
row 0 → row 1 → row 2
```

và:

```text
col 0 → col 1 → col 2
```

Đây chính là **topological ordering** của state graph.

---

# 22. Bước 7 — Xác định answer

Một lỗi phổ biến:

> `dp[n]` không phải lúc nào cũng là đáp án.

Ví dụ LIS với:

```text
dp[i] = LIS kết thúc tại i
```

thì đáp án là:

```text
max(dp)
```

chứ không nhất thiết là:

```text
dp[n-1]
```

Vì vậy phải hỏi:

> **Đáp án của bài toán tương ứng với state nào?**

---

# 23. Bước 8 — Tối ưu memory

Sau khi có DP đúng, mới nghĩ đến optimization.

Ví dụ:

```text
dp[i] = dp[i-1] + dp[i-2]
```

Ta không thực sự cần cả array.

Chỉ cần:

```text
prev2
prev1
current
```

Do đó:

```python
prev2 = 0
prev1 = 1

for i in range(2, n + 1):
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current
```

Từ:

```text
O(n) memory
```

xuống:

```text
O(1) memory
```

Nhưng:

> **Đừng tối ưu memory trước khi chắc chắn recurrence đúng.**

---

# 24. Một ví dụ hoàn chỉnh: House Robber

Hãy áp dụng toàn bộ triết lý.

Input:

```text
[2, 7, 9, 3, 1]
```

## Step 1 — State

Ta định nghĩa:

```text
dp[i] = số tiền lớn nhất có thể lấy từ nhà 0 đến nhà i
```

## Step 2 — Choices

Tại nhà `i`:

```text
Không lấy i
```

hoặc:

```text
Lấy i
```

## Step 3 — Transition

Nếu không lấy:

```text
dp[i-1]
```

Nếu lấy:

```text
nums[i] + dp[i-2]
```

Do đó:

```text
dp[i] = max(
    dp[i-1],
    nums[i] + dp[i-2]
)
```

## Step 4 — Base case

```text
dp[0] = nums[0]
```

Với hai nhà:

```text
dp[1] = max(nums[0], nums[1])
```

## Step 5 — Tính

```text
nums = [2, 7, 9, 3, 1]

dp[0] = 2

dp[1] = max(2, 7)
      = 7

dp[2] = max(7, 2 + 9)
      = 11

dp[3] = max(11, 7 + 3)
      = 11

dp[4] = max(11, 11 + 1)
      = 12
```

Kết quả:

```text
12
```

---

# 25. Điều gì khiến đây là DP chứ không chỉ là "công thức"?

Hãy nhìn kỹ.

Chúng ta đã làm:

```text
Problem
   ↓
State
   ↓
Subproblems
   ↓
Transitions
   ↓
Reuse results
   ↓
Final answer
```

Nếu không có việc **reuse kết quả của subproblem**, DP mất đi phần quan trọng nhất.

Nếu không có cách xây dựng bài toán lớn từ bài toán nhỏ, cũng không thể dùng DP.

---

# 26. DP không nhất thiết phải có recursion

Đây là một misconception rất phổ biến.

DP có thể là:

### Recursive + Memoization

```python
def solve(state):
    if state in memo:
        return memo[state]

    ...
```

hoặc:

### Iterative + Tabulation

```python
for state in states:
    dp[state] = ...
```

Hoặc thậm chí DP có thể được implement theo nhiều cấu trúc khác.

Điều quan trọng **không phải syntax**.

Điều quan trọng là:

```text
State
+
Transition
+
Reuse
```

---

# 27. Một cách cực kỳ hữu ích để nhìn DP: "Decision Tree → DAG"

Hãy tưởng tượng bạn có một bài toán với các lựa chọn.

Ban đầu nó giống:

```text
                Start
              /       \
             A         B
           /  \       /  \
          C    D     C    E
```

Ta thấy:

```text
C
```

xuất hiện hai lần.

Nếu coi mỗi lần xuất hiện là một bài toán riêng:

```text
Tree
```

ta sẽ tính lại.

Nhưng nếu nhận ra hai `C` thực chất là **cùng một state**, ta gộp chúng:

```text
                Start
              /       \
             A         B
              \       /
                C
               / \
              D   E
```

Bây giờ cấu trúc trở thành:

```text
DAG
```

và ta chỉ tính `C` một lần.

**Đây là một cách nhìn cực sâu về DP.**

---

# 28. Vì vậy, khi nhìn một bài toán, hãy tìm "state compression"

Đây là một khái niệm quan trọng.

Ví dụ bạn có thể có hàng triệu cách đi qua một bài toán.

Nhưng rất nhiều cách trong số đó cuối cùng rơi vào cùng một state.

Ví dụ:

```text
Path A → state (i, j)
Path B → state (i, j)
Path C → state (i, j)
Path D → state (i, j)
```

Nếu tất cả những path này có cùng:

```text
(i, j)
```

và tương lai chỉ phụ thuộc vào `(i, j)`, thì chúng ta **không cần quan tâm quá khứ cụ thể là gì nữa**.

Chỉ cần:

```text
dp[i][j]
```

Đây là một trong những lý do DP mạnh đến vậy.

---

# 29. Đây cũng là nguyên lý "History Independence"

Một state tốt thường có tính chất:

> **Một khi đã biết state hiện tại, lịch sử dẫn tới state đó không còn quan trọng đối với phần còn lại của bài toán.**

Ví dụ:

```text
A → B → C
X → Y → C
P → Q → C
```

Nếu từ `C` trở đi, mọi thứ giống hệt nhau, thì:

```text
C
```

là một state duy nhất.

Không cần biết:

```text
A → B
X → Y
P → Q
```

đã xảy ra thế nào.

Đây chính là lý do chúng ta có thể "nén" vô số trường hợp thành một state.

---

# 30. Vậy làm sao biết state của mình đã đủ?

Hãy tự hỏi:

> **Nếu hai cách khác nhau dẫn tới cùng state của tôi, liệu tương lai của chúng có luôn giống nhau không?**

Nếu **có**:

```text
state đủ thông tin
```

Nếu **không**:

```text
state thiếu thông tin
```

Đây là một test cực kỳ mạnh.

Ví dụ bạn định nghĩa:

```text
dp[i] = answer khi đang ở index i
```

Nhưng thực tế tương lai còn phụ thuộc vào:

```text
đã chọn bao nhiêu item
```

thì:

```text
dp[i]
```

không đủ.

Bạn phải thêm:

```text
dp[i][count]
```

---

# 31. Một ví dụ về state thiếu thông tin

Giả sử bài toán:

> Chọn các item, tối đa được `k` item.

Nếu bạn chỉ lưu:

```text
dp[i]
```

với:

```text
i = index
```

thì không biết trước đó đã chọn bao nhiêu item.

Hai trường hợp:

```text
đến i sau khi chọn 2 item
```

và:

```text
đến i sau khi chọn 5 item
```

có tương lai khác nhau.

Vậy phải lưu:

```text
dp[i][k]
```

hoặc một state tương đương.

---

# 32. Đây là lý do DP có thể có rất nhiều chiều

Bạn sẽ gặp:

```text
dp[i]
```

1D

```text
dp[i][j]
```

2D

```text
dp[i][j][k]
```

3D

thậm chí:

```text
dp[mask][i]
```

hoặc:

```text
dp[left][right][k]
```

Không phải vì tác giả muốn code khó.

Mỗi chiều thường đại diện cho **một phần thông tin cần thiết của state**.

---

# 33. Bitmask DP cũng không khác bản chất

Ví dụ:

```text
dp[mask][i]
```

có thể nghĩa là:

> Chi phí nhỏ nhất để đã thăm các node trong `mask` và hiện đang đứng ở `i`.

Ở đây:

```text
mask
```

là state information.

```text
i
```

là state information.

Vẫn là:

```text
State
→ Transition
→ Reuse
```

Không có "loại DP thần bí" nào cả.

---

# 34. Từ đó có thể phân loại DP theo State

Bạn sẽ thấy các pattern:

### 1D DP

```text
dp[i]
```

Ví dụ:

```text
Climbing Stairs
House Robber
```

### 2D Grid DP

```text
dp[i][j]
```

Ví dụ:

```text
Unique Paths
Minimum Path Sum
```

### Knapsack

```text
dp[item][capacity]
```

### String DP

```text
dp[i][j]
```

### Interval DP

```text
dp[left][right]
```

### State Machine DP

```text
dp[day][state]
```

### Bitmask DP

```text
dp[mask][position]
```

### Tree DP

```text
dp[node][state]
```

### Digit DP

```text
dp[position][state][tight][...]
```

Nhìn bên ngoài rất khác nhau.

Nhưng bên trong đều là cùng một triết lý.

---

# 35. DP và Greedy khác nhau thế nào?

Đây là một điểm rất quan trọng.

### Greedy

Tại mỗi bước:

> Chọn phương án tốt nhất **ngay lúc này**.

Hy vọng nó dẫn tới lời giải tối ưu toàn cục.

Ví dụ:

```text
chọn coin lớn nhất trước
```

### DP

Không tin rằng một lựa chọn local là đủ.

Nó xem xét các state:

```text
state A
state B
state C
...
```

và lưu kết quả tốt nhất cho từng state.

Nói đơn giản:

> **Greedy cố gắng quyết định ngay. DP cố gắng hiểu không gian các trạng thái.**

---

# 36. DP và Divide & Conquer khác nhau thế nào?

Cả hai đều chia bài toán thành bài toán nhỏ.

Nhưng:

### Divide & Conquer

Thường có các subproblem **độc lập**.

Ví dụ Merge Sort:

```text
array
├── left
└── right
```

Hai phần gần như độc lập.

### DP

Các subproblem thường **overlap**.

Ví dụ:

```text
fib(5)
├── fib(4)
│   └── fib(3)
└── fib(3)
```

`fib(3)` được dùng lại.

Do đó:

```text
Divide & Conquer
→ chia nhỏ và giải

DP
→ chia nhỏ + nhận ra overlap + lưu kết quả
```

---

# 37. Một cách tư duy rất mạnh: "What is the last decision?"

Khi gặp DP mới, một câu hỏi cực hữu ích là:

> **Quyết định cuối cùng của lời giải là gì?**

Ví dụ House Robber:

```text
Nhà cuối cùng:
take / don't take
```

LCS:

```text
ký tự cuối:
match / skip
```

Knapsack:

```text
item cuối:
take / don't take
```

Coin Change:

```text
coin cuối cùng là coin nào?
```

Interval DP:

```text
phần tử nào được chọn làm điểm chia cuối?
```

Khi tìm được "last decision", transition thường bắt đầu lộ ra.

---

# 38. Một framework bạn có thể dùng cho mọi bài DP

Khi mở một bài LeetCode DP, hãy viết ra giấy:

```text
1. What is my state?

2. What does dp[state] mean?

3. What decisions can I make?

4. Where can this state come from?

5. What is the transition?

6. What are the base cases?

7. In what order should states be computed?

8. Where is the final answer?

9. Can memory be optimized?
```

Nếu bạn trả lời được cả 9 câu này, gần như bạn đã **solve được DP về mặt tư duy**.

Code chỉ còn là bước translate.

---

# 39. Một ví dụ sâu hơn: Coin Change

Bạn có:

```text
coins = [1, 2, 5]
amount = 11
```

Muốn số coin ít nhất.

## State

```text
dp[x] = số coin ít nhất để tạo ra amount x
```

## Last decision

Coin cuối cùng có thể là:

```text
1
2
5
```

Nếu coin cuối là `5`, trước đó phải tạo được:

```text
x - 5
```

Do đó:

```text
dp[x] = min(
    dp[x-1] + 1,
    dp[x-2] + 1,
    dp[x-5] + 1
)
```

Tổng quát:

```text
dp[x] = min(
    dp[x - coin] + 1
)
```

với mọi `coin`.

## Base

```text
dp[0] = 0
```

Vì để tạo amount `0`, cần 0 coin.

Đây là một ví dụ rất đẹp của tư duy:

```text
Final decision
     ↓
Remove final decision
     ↓
Smaller problem
     ↓
Solve smaller problem
     ↓
Add final decision back
```

---

# 40. Đây gần như là công thức triết học của DP

Bạn có thể nhớ:

> **"Take a solution, remove its last decision, and ask what smaller problem remains."**

Sau đó:

```text
Smaller problem
       ↓
Best solution
       ↓
Add current decision
       ↓
Current best solution
```

Đây là cách rất tự nhiên để tìm recurrence.

---

# 41. Một thuật toán DP hoàn chỉnh thực chất có 4 thành phần toán học

Nếu bỏ hết code đi, DP thường chỉ còn:

### 1. State space

Tập hợp tất cả state có thể tồn tại.

```text
S
```

### 2. Transition

State nào có thể đi tới state nào.

```text
s → s'
```

### 3. Base values

Giá trị của những state ban đầu.

```text
dp[s] = ...
```

### 4. Aggregation

Cách kết hợp các transition.

Ví dụ:

```text
max
min
sum
count
```

Đây là lý do DP có thể giải:

* maximization
* minimization
* counting
* probability
* feasibility

chứ không chỉ tìm "max".

---

# 42. DP không chỉ là "max/min"

Có 4 dạng rất phổ biến:

### Optimization

```text
maximum / minimum
```

Ví dụ:

```text
House Robber
Coin Change
```

### Counting

```text
how many ways?
```

Ví dụ:

```text
Climbing Stairs
Coin Change II
```

### Feasibility

```text
có thể hay không?
```

Ví dụ:

```text
Partition Equal Subset Sum
```

State thường là:

```text
True / False
```

### Probability / Expected value

Các bài nâng cao có thể có:

```text
dp[state] = probability
```

Nhưng triết lý vẫn không đổi.

---

# 43. Một dấu hiệu cực mạnh để nhận ra DP

Khi đề bài có những từ như:

```text
maximum
minimum
number of ways
possible
longest
shortest
best
optimal
```

và đồng thời có:

```text
choices
subarrays
substrings
subsets
sequence
steps
states
```

hãy nghĩ đến DP.

Nhưng đừng kết luận ngay.

Hãy kiểm tra:

```text
Có state nhỏ hơn không?
Có overlap không?
Có transition rõ ràng không?
```

---

# 44. Một điều cực kỳ quan trọng: DP không phải "mẹo"

Nhiều người học DP theo kiểu:

```text
Thấy climbing stairs → nhớ công thức

Thấy house robber → nhớ công thức

Thấy coin change → nhớ công thức
```

Cách này rất dễ thất bại khi đề thay đổi.

Cách tốt hơn là học:

```text
Pattern
↓
State
↓
Transition
```

Ví dụ sau khi hiểu Knapsack, bạn sẽ nhận ra rất nhiều bài:

```text
416
494
1049
474
879
```

thực chất là những biến thể của cùng một framework.

---

# 45. Cấp độ tư duy cao nhất: DP là "State Design"

Khi bạn mới học:

> "DP là dùng mảng để lưu kết quả."

Khi hiểu hơn:

> "DP là tìm recurrence."

Khi giỏi:

> "DP là thiết kế state."

Khi rất giỏi:

> **"DP là tìm một biểu diễn state đủ nhỏ nhưng đủ thông tin để toàn bộ tương lai của bài toán phụ thuộc chỉ vào state đó."**

Đây mới là tư duy quan trọng.

---

# 46. Từ đó, có một nguyên tắc vàng

Mình muốn bạn nhớ câu này:

> **State phải là "minimal sufficient information".**

Tức là:

**Đủ** để biết tương lai.

Nhưng **không dư**.

Ví dụ:

```text
dp[i][j][k][x][y][z]
```

có thể đúng, nhưng nếu `x`, `y`, `z` không cần thiết thì state đang quá lớn.

State càng lớn:

```text
Time ↑
Memory ↑
```

Do đó người giỏi DP thường cố tìm:

```text
minimum information
```

để mô tả state.

---

# 47. Đây cũng là lý do tối ưu DP thường khó

Ví dụ ban đầu:

```text
dp[i][j][k]
```

có:

```text
O(nmk)
```

states.

Sau khi hiểu bài toán sâu hơn, có thể nhận ra `k` không cần thiết:

```text
dp[i][j]
```

và giảm xuống:

```text
O(nm)
```

Hoặc nhận ra chỉ cần layer trước:

```text
dp[j]
```

và memory từ:

```text
O(nm)
```

xuống:

```text
O(m)
```

Optimization không chỉ là "code clever".

Nó thường bắt đầu từ việc **hiểu dependency giữa các states**.

---

# 48. Tóm tắt toàn bộ Dynamic Programming

Bạn có thể đóng gói DP thành sơ đồ này:

```text
                    PROBLEM
                       │
                       ▼
              Có bài toán con?
                       │
                       ▼
              Các bài toán con
                 có overlap?
                       │
                       ▼
                DESIGN STATE
                       │
                       ▼
         State có đủ thông tin không?
                       │
                       ▼
              DEFINE TRANSITION
                       │
                       ▼
                BASE CASE
                       │
                       ▼
             COMPUTATION ORDER
                       │
                       ▼
                 FINAL ANSWER
                       │
                       ▼
              MEMORY OPTIMIZATION
```

Và nếu rút gọn hơn nữa:

```text
       STATE
         │
         ▼
    TRANSITION
         │
         ▼
     BASE CASE
         │
         ▼
      ANSWER
```

---

# 49. "Công thức" để tự tạo một DP

Khi gặp bài mới, hãy tự nói thành tiếng:

> **"Tôi muốn biết X."**

Ví dụ:

```text
Tôi muốn biết số cách để tới i.
```

→ `dp[i]`

Sau đó:

> **"Để biết X ở hiện tại, tôi cần biết những X nào trước đó?"**

→ transition.

Sau đó:

> **"Quyết định cuối cùng của tôi là gì?"**

→ choices.

Sau đó:

> **"State nhỏ nhất là gì?"**

→ base case.

Cuối cùng:

> **"Tất cả state cần tính theo thứ tự nào?"**

→ iteration / topological order.

Nếu làm được chuỗi suy luận này, bạn không còn phụ thuộc vào việc nhớ template nữa.

---

# 50. Và đây là điều mình muốn bạn đạt được khi luyện LeetCode DP

Đừng đặt mục tiêu:

> "Tôi muốn thuộc 50 bài DP."

Hãy đặt mục tiêu:

> **"Tôi muốn nhìn một bài mới và tự thiết kế được state."**

Ví dụ gặp:

```text
House Robber
```

Bạn nhận ra:

```text
i
```

Gặp:

```text
LCS
```

Bạn nhận ra:

```text
i, j
```

Gặp:

```text
Knapsack
```

Bạn nhận ra:

```text
item, capacity
```

Gặp:

```text
Stock
```

Bạn nhận ra:

```text
day, holding, transactions
```

Gặp:

```text
Burst Balloons
```

Bạn nhận ra:

```text
left, right
```

Gặp:

```text
Shortest Path Visiting All Nodes
```

Bạn nhận ra:

```text
visited mask, current node
```

**Đó mới là dấu hiệu bạn thực sự hiểu DP.**

---

## Cuối cùng, hãy nhớ 5 câu hỏi này

Mỗi khi gặp một bài DP mới, **đừng code ngay**. Viết ra:

```text
1. State của mình là gì?

2. dp[state] có nghĩa chính xác là gì?

3. Từ state này có những lựa chọn nào?

4. Transition từ các state nhỏ hơn sang state này là gì?

5. Base case là gì?
```

Nếu 5 câu này rõ ràng, phần code thường chỉ còn là việc triển khai.

**Nếu phải chọn duy nhất một kỹ năng để tập trung khi học DP, hãy chọn "state design".** Nó là chiếc cầu nối từ việc *làm theo template* sang việc *tự giải được một bài DP chưa từng gặp*.
