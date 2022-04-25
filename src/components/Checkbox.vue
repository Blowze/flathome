<template>
    <Ripple>
        <div class="CheckboxWrap">
            <label class="Checkbox">
                <input type="checkbox" name="peas" />
                <div class="CheckboxMain">
                    <span class="label"> {{ text }} </span>
                </div>
            </label>
        </div>
    </Ripple>
</template>

<script>
import Ripple from "./Ripple.vue";

export default {
    name: "CheckboxDefault",
    components: {
        Ripple,
    },
    props: {
        text: String,
        status: String,
        name: String,
        region: String,
    },
};
</script>

<style scoped lang="scss" >
.Checkbox {
    display: flex;
    flex-direction: column;
    justify-content: center;
    position: relative;
    padding-left: 54px;
    text-align: left;
    min-height: 46px;
    padding-top: 8px;
    padding-bottom: 8px;

    line-height: 20px;
    color: var(--tg-theme-text-color);
    cursor: pointer;
    font-weight: 500;
    &:last-child {
        margin-bottom: 0;
    }
    input {
        position: absolute;
        z-index: -1;
        opacity: 0;
    }
    .CheckboxMain {
        &::before,
        &::after {
            content: "";
            display: block;
            position: absolute;
            left: 2px;
            top: 50%;
            transform: translateY(-50%);
            width: 16px;
            height: 16px;
        }

        &::before {
            border: 2px solid var(--color-border-input);
            border-radius: 0.25rem;
            background-color: var(--color-background);
            transition: border-color 0.1s ease, background-color 0.1s ease;
        }

        &::after {
            /* stylelint-disable-next-line scss/operator-no-unspaced */
            background: center no-repeat
                url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTIiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+PHBhdGggZD0iTTEzLjkuOEw1LjggOC45IDIuMSA1LjJjLS40LS40LTEuMS0uNC0xLjYgMC0uNC40LS40IDEuMSAwIDEuNkw1IDExLjJjLjQuNCAxLjEuNCAxLjYgMGw4LjktOC45Yy40LS40LjQtMS4xIDAtMS42LS41LS40LTEuMi0uNC0xLjYuMXoiIGZpbGw9IiNGRkYiIGZpbGwtcnVsZT0ibm9uemVybyIvPjwvc3ZnPg==);
            background-size: 0.875rem;
            opacity: 0;
            transition: opacity 0.1s ease;
            width: 20px;
            height: 20px;
        }

        .label {
            display: block;
            text-align: initial;
        }
    }

    input:checked ~ .CheckboxMain {
        &::before {
            border-color: var(--tg-theme-button-color);
            background-color: var(--tg-theme-button-color);
        }

        &::after {
            opacity: 1;
        }
    }

    &[dir="rtl"] {
        padding-left: 0;
        padding-right: 4.5rem;

        .label {
            text-align: right;
        }

        .CheckboxMain {
            &::before,
            &::after {
                left: auto;
                right: 1.1875rem;
            }
        }
    }
}
.CheckboxWrap {
    padding-left: var(--space-normal);
    padding-right: var(--space-normal);
}
</style>
