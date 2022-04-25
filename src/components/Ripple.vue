<template>
    <div class="Ripple" data-ripple-color="#FFF" @click="animateButton($event)">
        <slot></slot>
    </div>
</template>

<script>
export default {
    name: "RippleWrap",
    methods: {
        animateButton(e) {
            // If possible, correct
            const ripple = document.createElement("i");
            ripple.classList.add("animation-ripple");
            const rippleOffset = e.currentTarget.getBoundingClientRect();
            const rippleY = e.pageY - rippleOffset.top;
            const rippleX = e.pageX - rippleOffset.left;
            // eslint-disable-next-line no-sequences
            (ripple.style.top = `${rippleY}px`),
                (ripple.style.left = `${rippleX}px`),
                (ripple.style.background =
                    e.currentTarget.getAttribute("data-ripple-color"));
            e.currentTarget.appendChild(ripple);
            setTimeout(() => {
                ripple.parentNode.removeChild(ripple);
            }, 400);
        },
    },
};
</script>

<style scoped lang="scss" >
.Ripple {
    overflow: hidden;
    width: 100%;
    position: relative;
}
</style>
