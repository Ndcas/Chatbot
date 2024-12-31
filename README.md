Python 3.9.13

Rasa 3.6.20

Cài đặt:

    python -m venv ./venv

    ./venv/Scripts/activate

    pip install rasa

    pip install -U randomname

Chạy:

    cd rasaproject

    rasa run actions (terminal 1)    

    rasa shell (terminal 2)

Huấn luyện lại (xóa cache trước):

    rmdir models

    rasa train

Kiểm tra các chỉ số sau khi huấn luyện:

    tensorboard --logdir .\tensorboard\

    Mở link được hiện trong terminal
