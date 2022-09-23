FROM animcogn/face_recognition:gpu

RUN useradd -ms /bin/bash adhi && \
    chown -R adhi:adhi /opt/iu && \
    echo 'PATH="/opt/venv/bin:$PATH"' >> /home/adhi/.bashrc

USER adhi

ENV PATH="/opt/venv/bin:$PATH"

RUN pip3 install jupyterlab

ENV NB_PREFIX /

CMD ["sh", "-c", "jupyter lab --notebook-dir=/home/jovyan --ip=0.0.0.0 --no-browser --allow-root --port=8888 --NotebookApp.token='' --NotebookApp.password='' --NotebookApp.allow_origin='*' --NotebookApp.base_url=${NB_PREFIX}"]
