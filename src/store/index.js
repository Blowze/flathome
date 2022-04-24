import city from "./city/state";

const store = {
    modules: {
        city: {
            namespaced: true,
            state: () => city(),
            mutations: {
                SET_SELECT(state, item) {
                    state.curent = item;
                },
                SET_SELECT_REGION(state, item) {
                    state.regionCurrent = item;
                },
            },
        },
        cityCurrent: {},
        regionCurrent: {},
    },
};

export default store;
