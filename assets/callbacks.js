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
    },
    curriculum_click: function(...args) {
        const ctx = dash_clientside.callback_context.triggered[0]['prop_id'].substring(12, 14);
        const imageURL = "assets/cv/Pedro Kobori CV-" + ctx + ".pdf";
        fetch(imageURL)
            .then(response => response.blob())
            .then(blob => {
                const blobUrl = window.URL.createObjectURL(blob);
                const link = document.createElement("a");
                link.href = blobUrl;
                link.download = 'Pedro Kobori CV ' + ctx + '.pdf';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
                window.URL.revokeObjectURL(blobUrl);
            })
            .catch(console.error);
        return window.dash_clientside.no_update;
    }
}
