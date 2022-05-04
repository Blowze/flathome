<template>
    <div
        class="RippleHandler"
        data-ripple-color="#FFF"
        @click="animateButton($event)"
    >
        <slot></slot>
        <span class="RippleMask">
            <span class="Ripple"></span>
        </span>
    </div>
</template>

<script>
export default {
    name: "RippleWrap",
    methods: {
        animateButton() {
            if (!document.querySelectorAll) return;
            const rippleHandlers = document.querySelectorAll(".RippleHandler");
            const redraw = function (el) {
                el.offsetTop + 1;
            };
            const isTouch = "ontouchstart" in window;
            for (let i = 0; i < rippleHandlers.length; i++) {
                (function (rippleHandler) {
                    function onRippleStart(e) {
                        const rippleMask =
                            rippleHandler.querySelector(".RippleMask");
                        let clientX;
                        let clientY;
                        if (!rippleMask) return;
                        const rect = rippleMask.getBoundingClientRect();
                        if (e.type === "touchstart") {
                            clientX = e.targetTouches[0].clientX;
                            clientY = e.targetTouches[0].clientY;
                        } else {
                            clientX = e.clientX;
                            clientY = e.clientY;
                        }
                        const rippleX =
                            clientX - rect.left - rippleMask.offsetWidth / 2;
                        const rippleY =
                            clientY - rect.top - rippleMask.offsetHeight / 2;
                        const ripple = rippleHandler.querySelector(".Ripple");
                        ripple.style.transition = "none";
                        redraw(ripple);
                        ripple.style.transform = `translate3d(${rippleX}px, ${rippleY}px, 0) scale3d(0.2, 0.2, 1)`;
                        ripple.style.opacity = 1;
                        redraw(ripple);
                        ripple.style.transform = `translate3d(${rippleX}px, ${rippleY}px, 0) scale3d(1, 1, 1)`;
                        ripple.style.transition = "";

                        function onRippleEnd() {
                            ripple.style.transitionDuration =
                                "var(--ripple-end-duration, .2s)";
                            ripple.style.opacity = 0;
                            if (isTouch) {
                                document.removeEventListener(
                                    "touchend",
                                    onRippleEnd
                                );
                                document.removeEventListener(
                                    "touchcancel",
                                    onRippleEnd
                                );
                            } else {
                                document.removeEventListener(
                                    "mouseup",
                                    onRippleEnd
                                );
                            }
                        }
                        if (isTouch) {
                            document.addEventListener("touchend", onRippleEnd);
                            document.addEventListener(
                                "touchcancel",
                                onRippleEnd
                            );
                        } else {
                            document.addEventListener("mouseup", onRippleEnd);
                        }
                    }
                    if (isTouch) {
                        rippleHandler.removeEventListener(
                            "touchstart",
                            onRippleStart
                        );
                        rippleHandler.addEventListener(
                            "touchstart",
                            onRippleStart
                        );
                    } else {
                        rippleHandler.removeEventListener(
                            "mousedown",
                            onRippleStart
                        );
                        rippleHandler.addEventListener(
                            "mousedown",
                            onRippleStart
                        );
                    }
                })(rippleHandlers[i]);
            }
        },
    },
};
</script>

<style scoped lang="scss" >
.RippleHandler {
    overflow: hidden;
    width: 100%;
    position: relative;
}
.RippleMask {
    border-radius: inherit;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    bottom: 0;
    transform: translateZ(0);
    overflow: hidden;
    pointer-events: none;
}
.Ripple {
    position: absolute;
    width: 200%;
    left: 50%;
    top: 50%;
    margin: -100% 0 0 -100%;
    padding-top: 200%;
    border-radius: 50%;
    background-color: rgba(0, 0, 0, 0.07);
    transition: transform var(--ripple-duration) ease-out,
        opacity var(--ripple-duration) ease-out,
        background-color var(--ripple-duration) ease-out;
    opacity: 0;
}
</style>
