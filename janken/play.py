HANDS = ('グー', 'チョキ', 'パー')


def select_hand():
    """
    コンピュータの手をランダムに決める
    :return: HANDSの中のいずれか
    """
    import random
    return random.choice(HANDS)

if select_hand() == 'グー':
    computer = 1

elif select_hand() == 'チョキ':
    computer = 2

else:
    computer = 3


def judgement(player, computer):
    """
    じゃんけんの勝敗を判定する。
    :param player: HANDSの中のどれか。
    :param computer: HANDSの中のどれか
    :return: プレイヤーが勝ちの場合は1,あいこは0,負けは-1を返す
    """

    if player == computer:
        return 0

    elif player == '1' and computer == 'パー':
        return -1

    elif player == '2' and computer == 'グー':
        return -1

    elif player == '3' and computer == 'チョキ':
        return -1

    else:
        return 1



def save_score(result):
    """
    'score.txt'に戦績を保存。
    win:x lose:y draw:zのディクショナリデータを保存する。
    :param result:HANDS
    :return: None
    """
    result = judgement(player, computer)
    if result == -1:
        return "y"
    elif result == 0:
        return "z"
    else:
        return "x"
    return None



if __name__ == '__main__':
    player = int(input('グー(1)/チョキ(2)/パー(3)を選んでください(数字):'))
    computer = select_hand()
    result = judgement(player, computer)
    # コンピュータの手と勝敗の結果を表示
    print("computer", computer)
    print(result)

    score = save_score(result)
    f = open("score.txt","a")
    f.write(score)
    f.close

