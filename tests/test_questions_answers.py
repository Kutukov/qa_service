from datetime import datetime


def test_create_question_and_answer(client):
    # создание вопроса
    resp = client.post("/questions/", json={"text": "Что такое FastAPI?"})
    assert resp.status_code == 201
    q = resp.json()
    qid = q["id"]

    # добавление первого ответа
    resp2 = client.post(
        f"/questions/{qid}/answers/",
        json={"user_id": "user-1", "text": "Это фреймворк"},
    )
    assert resp2.status_code == 201
    a1 = resp2.json()
    assert a1["question_id"] == qid
    assert a1["user_id"] == "user-1"

    # добавляние второго ответа
    resp3 = client.post(
        f"/questions/{qid}/answers/", json={"user_id": "user-2", "text": "Для API"}
    )
    assert resp3.status_code == 201
    a2 = resp3.json()

    # получаем вопрос с ответами
    resp4 = client.get(f"/questions/{qid}")
    assert resp4.status_code == 200
    data = resp4.json()
    assert len(data["answers"]) == 2

    # проверка формата created_at
    for answer in data["answers"]:
        datetime.fromisoformat(answer["created_at"].replace("Z", "+00:00"))

    # проверки валидации
    resp5 = client.post("/questions/", json={})
    assert resp5.status_code == 422  # отсутствует текст

    resp6 = client.post(
        "/questions/9999/answers/", json={"user_id": "u1", "text": "test"}
    )
    assert resp6.status_code == 404  # вопрос не найден

    # удаляем вопрос, чтобы проверить, что ответы удалились коскадно
    resp7 = client.delete(f"/questions/{qid}")
    assert resp7.status_code == 204

    # проверка, что ответы удалены после каскадного удаления
    resp8 = client.get(f"/answers/{a1['id']}")
    assert resp8.status_code == 404
    resp9 = client.get(f"/answers/{a2['id']}")
    assert resp9.status_code == 404

    # проверка, что вопрос удалён
    resp10 = client.get(f"/questions/{qid}")
    assert resp10.status_code == 404
