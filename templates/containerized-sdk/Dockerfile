FROM @CONTAINER_IMAGE_NAME@:@CONTAINER_IMAGE_TAG@

ARG uid
ARG http_proxy
ARG https_proxy
ARG no_proxy

RUN useradd -m sdkuser -u $uid 

USER sdkuser
CMD /bin/bash -l

