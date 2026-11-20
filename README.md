# My-Python-Learning-Journey
## Project Introduction 项目简介
### This repository is mainly used to store my Python learning materials — mostly code that I'm interested in and some that might be commonly useful. It's also an opportunity for me to explore more Python knowledge. <br>这个代码仓库主要是用来存放我在python上学习方面的内容，主要是我感兴趣和一些可能比较常用的代码，也是一个让我去接触更多关于python知识的机会。<br><br>

## Document User Handbook 文件说明
### ARTword.py：Basically, this code is a very simple program that generates a "text box" based on the text you input. When you want to create a more artistic text format, you can just type it in directly instead of spending a lot of time searching online. However, it still needs more styles added later. <br><br>基本上，这个代码是一个很简单，能够基于输入的文本生成“文本框”的代码，当你想要生成比较艺术的文本格式时，就可以直接输入，而不用花费很多时间在网上找，不过还需要后续增加更多的风格。<br>
### guessnum.py：This is a fun piece of code. It's essentially a number-guessing game where the number is between 1 and 100. The user gets 7 chances, and after each guess they receive feedback telling them whether their guess is larger or smaller than the target number. Depending on how many attempts it takes to guess correctly, they get a different comment :) <br>而这个是一个很有趣的代码，本质上是一个1-100的猜数字游戏，而用户会有7次机会，猜测后还会给予提示反馈，告诉用户他/她猜的数字比目标数字更大或更小，花不同次数猜对还会有不同评价：）。<br><br>

## Code Details 代码说明
### ARTword.py：这段代码就是一个"输入文字、画个框"，input("输入文字：") 负责接收你打的字，存进text。width = len(text) + 4 算出框的总宽度：len(text) 是文字长度，+4 是左右各留 2 格空格。接着三行 print 画框：第一行 "+" + "-" * width + "+" 用字符串乘法生成 width 个横线，两头加 + 当顶边框。第二行 "| " + text + " |" 是竖线加两个空格、文字、两个空格、竖线，当中间那行；第三行和第一行一样，画底边框。输入"你好"时 len 返回 2，width 是 6，所以画出 +------+ 的框。唯一要注意的地方就是 len() 按字符个数算，而Unicode里一个汉字实际占 2 格，所以中文框会偏窄、右边框对不齐，英文则完全正常。<br><br>

### guessnum.py：程序分两个函数：guess_number() 负责玩一局。先用 random.randint(1, 100) 生成目标数字，设 attempts = 0 和 max_attempts = 7。然后进入 while attempts < max_attempts 循环：每轮先 attempts += 1，用 try/except 包住 int(input(...)) 接收猜测，输入非数字时提示并 continue（不消耗次数）。接着用 if/elif/else 判断：等于目标就打印胜利信息和按次数分级的评价（1 次/≤3 次/≤5 次/其余）后 return 结束本局；小于目标提示"小了"，大于提示"大了"。循环结束后打印"机会用完了"并公布答案。main() 是外层循环：while True 里调用 guess_number() 玩一局，然后问"要再来一局吗"，.strip().lower() 后不是 y 就 break 退出。<br><br>

## Learning Insights & Further Plans 学习心得与规划
#### 借着这次作业才开始接触 Github，建立了这个代码仓库，也按自己兴趣试着写了两段代码，也看了看GitHub 上的一些其他Python和MATLAB代码，收获比预想的大。最大的感受还是关于看懂代码方面，代码的作者和读者都同样重要，作者要提供一些备注和说明，而作为读者也要具备足够的知识。在课堂上的时候觉得循环、判断和函数都还算明白的，但到了写代码才发现自己很容易出错。在写文本框程序的时候，就四行代码，可输入中文时右边框就是对不齐，琢磨之后才知道终端里汉字占两格、而 `len()`只是数字符数，而不是看字符占位数量。这种实践和亲自体会犯错的过程，比干看教程记得牢多了。现在我觉得，作为写代码的初学者，最怕的不是写错，而是不敢去尝试或者缺乏尝试的经验。作为刚接触 GitHub 的学生，说实话还在适应。第一次建仓库、第一次把代码传上去都格外迷茫。看别人的仓库，目录清清楚楚、README 写得明明白白、函数拆得也细，也让我开始有意识地给程序加注释、写说明，不再只是让它能跑就行。而在规划方面，我觉得之后会先补充文本框程序的内容，加几种不同风格的文本框以及能够给多行文本加上文本框，再继续完善仓库的说明。也可以在GitHub 上找一些和自己写的类似的代码，看看别人的代码有哪些更简洁或快捷的地方，从看别人的代码开始累积一些阅历。总的来说，还是以兴趣为先，去看和写一些自己感兴趣的、有意思的代码，然后慢慢积累更多经验，无论是写代码还是使用GitHub平台上都是。
