from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = {}

@app.route("/tasks", methods=["GET"])
def getTasksList():
    return jsonify(tasks), 200


@app.route("/tasks", methods=["POST"])
def addTask():
    global tasks
    data = request.get_json()
    if not data or not "title" or not "description":
        return jsonify({"Error": "New task needs a title and description."}), 400
    new_task = {"complete": False, "description": data["description"], "id":len(tasks)+1  ,"title": data["title"]}
    tasks[len(tasks)+1] = new_task
    return jsonify(new_task), 201


@app.route("/tasks/<int:task_id>", methods=["GET"])
def getTaskByID(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id]), 200
    return jsonify({"Error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def deleteTask(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({"Message": "Task deleted successfully"}), 200
    return jsonify({"Error": "Task not found"}), 404


@app.route("/tasks/<int:task_id>", methods=["PUT"])
def updateTask(task_id):
    if task_id not in tasks:
        return jsonify({"Error": "Task not found"}), 404
    data = request.get_json()
    if not data["title"] or not data["description"]:
        return jsonify({"Error": "Title and description required"}), 400
    task_to_update = tasks[task_id]
    task_to_update["title"] = data["title"]
    task_to_update["description"] = data["description"]
    tasks[task_id] = task_to_update
    return jsonify(task_to_update), 200


@app.route("/tasks/<int:task_id>/complete")
def completedTask(task_id):
    if task_id in tasks:
        tasks[task_id]["complete"] = True
        return jsonify({"Message": "Task marked as complete", "Task": tasks[task_id]}), 200
    return jsonify({"Error": "Task not found"}), 404

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5050)