# BlackJack (Chinese)

## blackjack_first_version

### 基本介绍

以 function 的形式实现了 Blackjack 的基本玩法。

- 初始资金是 5000，赌注必须小于等于 5000。
- 玩家如果抽到 A，可以每次自行选择将 A 当做 1 还是 11。
- 庄家抽到 A 时，如果按 11 计算不会爆牌，则自动按 11 计算。

### Hit / Stand / Double

- **Hit**：继续抽牌。
- **Stand**：本轮不再抽牌。
- **Double**：抽一张牌后进行比大小，赌注变为原来的 2 倍，并且不再继续抽牌。
- Double 必须在玩家第二次抽牌时选择；如果第三次或之后选择 Double，则该选择无效。
- 庄家达到 17 分及以上会自动 Stand。
- 如果玩家此时选择 Stand，则进入自动结算环节。

### 局限

- 牌池不会因为抽牌而减少，因此一轮中可能抽到多张相同花色和数字的牌。
- 玩法的交互以及 UI 比较简单。
- 每局第一轮游戏中(庄家和玩家首抽两牌时)，每抽一次牌都会重新显示一次牌桌。


# Blackjack (English)

This project contains two versions of a Blackjack game implemented in Python.

## First Version — `blackjack_first_version`

### Introduction

The first version implements the basic Blackjack gameplay using functions.

- Initial bankroll: **5000**.
- The bet must be less than or equal to **5000**.
- When the player draws an Ace, they can choose to count it as either **1 or 11** each time.
- When the dealer draws an Ace, it is automatically counted as **11** if doing so does not cause the dealer to bust.

### Hit / Stand / Double

- **Hit:** Continue drawing cards.
- **Stand:** Stop drawing cards for the current round.
- **Double:** Draw one additional card, double the bet, and then end the player's turn.
- Double is only valid when selected after the player's second card. If Double is selected after the third card or later, the choice is invalid.
- The dealer automatically stands when their score reaches **17 or higher**.
- When the player chooses Stand, the game proceeds to the automatic settlement process.

### Limitations

- The card pool is never reduced when cards are drawn. Therefore, the same card can appear multiple times in a single round.
- The gameplay interaction and UI are relatively basic.
- During the first round, the table is displayed again after each card is drawn.


---

## Final Version — `blackjck_final_version`

The final version implements the basic Blackjack gameplay using **classes**.

### Improvements

- The card pool is refreshed and reset at the beginning of each game.
- The table is displayed using a cleaner structure.
- The UI is more polished.
- The interaction is more visually intuitive.

### Limitations

- Ace handling is not implemented. All Aces are counted as **1**.
- The restriction that Double can only be selected after the player's second card is not implemented.
- Double still ends the player's turn after drawing one additional card.

### Difference from the First Version

In the final version, if the dealer's initial hand reaches **17 or higher**, the dealer automatically stands.

In addition, when the player makes their first **Hit / Stand / Double** decision, the dealer's card value is not displayed. This makes the game presentation closer to the conventional Blackjack interface.