def word_len(sentance):
    result = []          # აქ შეინახება საბოლოო შედეგი
    words = ""           # დროებითი ცვლადი სიტყვის ასაგებად

    for i in sentance:
        if i != " ":
            words += i   # ვაგროვებთ სიმბოლოებს სიტყვაში
        else:
            result.append(words + str(len(words)))  # ვამატებთ სიტყვას სიგრძით
            words = ""   # ვიწყებთ ახალ სიტყვას

    result.append(words + str(len(words)))  # ბოლო სიტყვის დამატება
    print(result)      # შედეგის დაბეჭდვა

