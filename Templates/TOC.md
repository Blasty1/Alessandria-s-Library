>[!SUMMARY] Table of Contents
<%*
    let headers = await tp.file.content
        .split('\n')
        .filter(t => t.match(/^[#]+\s+/gi))
        .map(h => {
            let header_level = h.split(' ')[0].match(/#/g).length;
            let header_text = h.substring(h.indexOf(' ') + 1).replace(/[\[\]]+/g, '');
            let header_link = `[[${tp.file.title}#${header_text}|${header_text}]]`;
            
            return `${'    '.repeat(header_level - 1) + '- ' + header_link}`;
        })
        .join('\n');
    
    tR += headers;
%>