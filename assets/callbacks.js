if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {
    display_page: function(hash) {
        if (hash === '') {
            return 'about';
        }
        return hash.slice(1);
    },
    certificate_click: function(...args) {
        const ctx = dash_clientside.callback_context.triggered[0]['prop_id'].substring(11, 14);
        const modalOutputs = Array(args.length).fill(false);
        modalOutputs[parseInt(ctx) - 1] = true;
        return modalOutputs;
    }
}