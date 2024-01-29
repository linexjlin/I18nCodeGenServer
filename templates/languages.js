var langs_data = {languages_json}

function requestOnline(k, l) {
    var url = "{api_addr}/{project_id}/key";

    var params = {
        k: k,
        l: l
    };
    fetch(url + "?" + new URLSearchParams(params))
        .then(response => {
            if (response.ok) {
                return response.json();
            } else {
                console.log("Failed to get data. Status code: " + response.status);
                return null;
            }
        })
        .then(data => {
            if (data) {
                var result = data.result;
                return result;
            } else {
                return k;
            }
        })
        .catch(error => console.log(error));
}

function UText(k) {
    var l = process.env.ULANG ? process.env.ULANG : "fr";
    if (langs_data.hasOwnProperty(k)) {
        if (langs_data[k].hasOwnProperty(l)) {
            return langs_data[k][l] ? langs_data[k][l] : k;
        } else {
            console.log("not supported lang: " + l);
            requestOnline(k, l);
            return k;
        }
    } else {
        requestOnline(k, l);
        return k;
    }
}