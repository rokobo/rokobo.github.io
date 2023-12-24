if (!window.dash_clientside) {
    window.dash_clientside = {};
}

window.dash_clientside.clientside = {
    certificate_click: function(...args) {
        const ctx = dash_clientside.callback_context.triggered[0]['prop_id'].substring(11, 14);
        const modalOutputs = Array(args.length).fill(false);
        modalOutputs[parseInt(ctx)] = true;
        return modalOutputs;
    },
    project_click: function(...args) {
        const ctx = dash_clientside.callback_context.triggered[0]['prop_id'].substring(11, 14);
        const modalOutputs = Array(args.length).fill(false);
        modalOutputs[parseInt(ctx)] = true;
        return modalOutputs;
    }
}
