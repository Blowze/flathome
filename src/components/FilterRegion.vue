<template>
    <div class="FilterRegion">
        <div class="FilterRegion__City">
            <div class="FilterRegion__Container">
                <div class="FilterRegion__Item">
                    <div class="FilterRegion__Avatar">
                        <img :src="image" />
                    </div>
                    <div class="FilterRegion__Info">
                        <!-- <div class="FilterRegion__Status">Ваш город:</div> -->
                        <div class="FilterRegion__Title">
                            {{ name }}
                        </div>
                    </div>
                </div>
                <button class="FilterRegion__Icon">
                    <span class="icon-cog"></span>
                </button>
            </div>
        </div>
        <div class="FilterRegion__Region" @click="selectRegion">
            <div class="FilterRegion__RegionInfo">{{ region }}</div>
            <div class="FilterRegion__Icon">
                <div class="icon-arrow-right2"></div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "FilterRegion",
    props: {
        image: String,
        status: String,
        name: String,
        region: String,
    },
    methods: {},
};
</script>

<style scoped lang="scss" >
.FilterRegion {
    max-width: 480px;
    width: 100%;
    margin: auto;
    background: var(--tg-theme-bg-color);
    box-shadow: 0px 1px 3px 0px rgba(0, 0, 0, 0.12);
    border-bottom: 1px solid var(--color-border-item);
    &__Avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        overflow: hidden;
        margin-right: 18px;
        img {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
    }
    &__Title {
        line-height: normal;
        font-size: 20px;
        font-weight: 500;
        color: var(--tg-theme-text-color);
    }
    &__Status {
        font-size: 12px;
        margin-bottom: 2px;
        color: var(--tg-theme-hint-color);
    }
    &__Item {
        display: flex;
        align-items: center;
        width: 100%;
    }
    &__Icon {
        margin-left: 8px;
        width: 30px;
        height: 30px;

        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 50%;
        background: transparent;
        border: none;
        color: var(--tg-theme-hint-color);
        padding: 0;
        min-width: 30px;
        cursor: pointer;
        font-size: 16px;
    }
    &__Region {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 4px var(--space-normal);
        padding-right: 10px;
        color: var(--tg-theme-hint-color);
        font-size: 14px;
        cursor: pointer;
        min-height: 40px;
        display: none;

        &:hover,
        &:focus,
        &:active {
            background: var(--color-background);
        }
    }
    &__RegionInfo {
        font-weight: 500;
        font-size: 12px;
    }
    &__Container {
        display: flex;
        align-items: center;
        padding: 8px;
        padding-left: 16px;
        padding-right: 10px;
        cursor: pointer;
        &:hover,
        &:focus,
        &:active {
            background: var(--color-background);
        }
    }
}
</style>
