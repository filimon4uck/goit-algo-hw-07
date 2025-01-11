class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replice = []
        self.isDeleted = False

    def add_reply(self, reply):
        self.replice.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.isDeleted = True

    def display(self, depth=0):
        indent = "_____" * depth

        text = (
            f"{self.author} : {self.text}"
            if not self.isDeleted
            else f"deleted:  {self.text}"
        )
        print(f"{indent}{text}")
        for reply in self.replice:
            reply.display(depth + 1)


def main():
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()


if __name__ == "__main__":
    main()
