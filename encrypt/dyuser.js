function getRandom(min, max){
    return Math.round(Math.random()*(max-min)+min)
}

function get_signature(uid) {

    module = undefined;
    exports = undefined;
    document = {};
    a1 = getRandom(60, 90)
    a3 = getRandom(3600, 4500)
    a4 = getRandom(100, 300)
    v1 = getRandom(400, 600)
    v2 = getRandom(30, 40)
    global.screen = {};
    global.navigator = {
        userAgent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+v1+'.'+v2+' (KHTML, like Gecko) Chrome/'+a1+'.0.'+a3+'.'+a4+' Safari/'+v1+'.'+v2+'',
        appCodeName: "Mozilla",
        appName: "Netscape",
        appVersion: '5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/'+v1+'.'+v2+' (KHTML, like Gecko) Chrome/'+a1+'.0.'+a3+'.'+a4+' Safari/'+v1+'.'+v2+'',
        cookieEnabled: true,
        deviceMemory: 8,
        doNotTrack: null,
        hardwareConcurrency: 8,
        language: "zh-CN",
        maxTouchPoints: 0,
        onLine: true,
        platform: "win32",
        product: "Gecko",
        productSub: "20030107",
        vendor: "Google Inc.",
        vendorSub: "",
        webdriver: false,
        bluetooth: {},
        clipboard: {},
    }
    global.location = {
        hash: "",
        host: "www.iesdouyin.com",
        hostname: "www.iesdouyin.com",
        origin: "https://www.iesdouyin.com",
        pathname: "/share/user/"+uid+"",
        port: "",
        protocol: "https:",
        protocol: "chrome:",
    }
    nu = function (a) {
        return undefined
    }
    canvas_2d = {
        fillText: function (a) {
            return undefined
        },
        arc: nu,
        stroke: nu
    }
    canvas = {
        getContext: function (a) {
            return canvas_2d
        },
        toDataURL: function () {
            return "data:image/png;base64,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"
        }
    }
    global.document = {
        createElement: function (a) {
            return canvas
        },
        // referrer: 'https://www.iesdouyin.com/share/user/2471313590452925?u_code=hmg91a3m&sec_uid=MS4wLjABAAAAedINtgUfnZBaBV_UQogK-blY5LrIjaok_KLUNNWQtShR_qUPX2EQTDutwIIyZQyo&did=MS4wLjABAAAA1f6vR5OORbcV7dZoQPLs4txtlS9k2ZnAiR51r6-S0SxAk-ITLaqNpAqTi3vpSeLK&iid=MS4wLjABAAAAvA6D_bP8mZPH32xMWT7zdaDqgOO7ppwRqcjxVoEwrWWMxAh_iW7DtQNbAxkspCQs&with_sec_did=1&app=douyin_lite&utm_campaign=client_share&utm_medium=ios&tt_from=copy&utm_source=copy',
        // cookie: '_tea_utm_cache_1243={%22utm_source%22:%22copy%22%2C%22utm_medium%22:%22ios%22%2C%22utm_campaign%22:%22client_share%22}',
        // URL: "https://www.iesdouyin.com/share/user/"+uid+"?u_code=hmg91a3m&sec_uid=MS4wLjABAAAAedINtgUfnZBaBV_UQogK-blY5LrIjaok_KLUNNWQtShR_qUPX2EQTDutwIIyZQyo&did=MS4wLjABAAAA1f6vR5OORbcV7dZoQPLs4txtlS9k2ZnAiR51r6-S0SxAk-ITLaqNpAqTi3vpSeLK&iid=MS4wLjABAAAAvA6D_bP8mZPH32xMWT7zdaDqgOO7ppwRqcjxVoEwrWWMxAh_iW7DtQNbAxkspCQs&with_sec_did=1&app=douyin_lite&utm_campaign=client_share&utm_medium=ios&tt_from=copy&utm_source=copy",
        // baseURI: "https://www.iesdouyin.com/share/user/"+uid+"?u_code=hmg91a3m&sec_uid=MS4wLjABAAAAedINtgUfnZBaBV_UQogK-blY5LrIjaok_KLUNNWQtShR_qUPX2EQTDutwIIyZQyo&did=MS4wLjABAAAA1f6vR5OORbcV7dZoQPLs4txtlS9k2ZnAiR51r6-S0SxAk-ITLaqNpAqTi3vpSeLK&iid=MS4wLjABAAAAvA6D_bP8mZPH32xMWT7zdaDqgOO7ppwRqcjxVoEwrWWMxAh_iW7DtQNbAxkspCQs&with_sec_did=1&app=douyin_lite&utm_campaign=client_share&utm_medium=ios&tt_from=copy&utm_source=copy",
        // documentURI: "https://www.iesdouyin.com/share/user/"+uid+"?u_code=hmg91a3m&sec_uid=MS4wLjABAAAAedINtgUfnZBaBV_UQogK-blY5LrIjaok_KLUNNWQtShR_qUPX2EQTDutwIIyZQyo&did=MS4wLjABAAAA1f6vR5OORbcV7dZoQPLs4txtlS9k2ZnAiR51r6-S0SxAk-ITLaqNpAqTi3vpSeLK&iid=MS4wLjABAAAAvA6D_bP8mZPH32xMWT7zdaDqgOO7ppwRqcjxVoEwrWWMxAh_iW7DtQNbAxkspCQs&with_sec_did=1&app=douyin_lite&utm_campaign=client_share&utm_medium=ios&tt_from=copy&utm_source=copy",
        domain: "www.iesdouyin.com",
    };
    window = global;
    window.top = window;


    var modules = {
        "9bd2804c7e68ac461d65":
        /***/
            (function (module, exports) {
                Function(function (t) {
                    return 'e(e,a,r){(b[e]||(b[e]=t("x,y","x "+e+" y")(r,a)}a(e,a,r){(k[r]||(k[r]=t("x,y","new x[y]("+Array(r+1).join(",x[y]")(1)+")")(e,a)}r(e,a,r){n,t,s={},b=s.d=r?r.d+1:0;for(s["$"+b]=s,t=0;t<b;t)s[n="$"+t]=r[n];for(t=0,b=s=a;t<b;t)s[t]=a[t];c(e,0,s)}c(t,b,k){u(e){v[x]=e}f{g=,ting(bg)}l{try{y=c(t,b,k)}catch(e){h=e,y=l}}for(h,y,d,g,v=[],x=0;;)switch(g=){case 1:u(!)4:f5:u((e){a=0,r=e;{c=a<r;c&&u(e[a]),c}}(6:y=,u((y8:if(g=,lg,g=,y===c)b+=g;else if(y!==l)y9:c10:u(s(11:y=,u(+y)12:for(y=f,d=[],g=0;g<y;g)d[g]=y.charCodeAt(g)^g+y;u(String.fromCharCode.apply(null,d13:y=,h=delete [y]14:59:u((g=)?(y=x,v.slice(x-=g,y:[])61:u([])62:g=,k[0]=65599*k[0]+k[1].charCodeAt(g)>>>065:h=,y=,[y]=h66:u(e(t[b],,67:y=,d=,u((g=).x===c?r(g.y,y,k):g.apply(d,y68:u(e((g=t[b])<"<"?(b--,f):g+g,,70:u(!1)71:n72:+f73:u(parseInt(f,3675:if(){bcase 74:g=<<16>>16g76:u(k[])77:y=,u([y])78:g=,u(a(v,x-=g+1,g79:g=,u(k["$"+g])81:h=,[f]=h82:u([f])83:h=,k[]=h84:!085:void 086:u(v[x-1])88:h=,y=,h,y89:u({e{r(e.y,arguments,k)}e.y=f,e.x=c,e})90:null91:h93:h=0:;default:u((g<<16>>16)-16)}}n=this,t=n.Function,s=Object.keys||(e){a={},r=0;for(c in e)a[r]=c;a=r,a},b={},k={};r'.replace(/[-]/g, function (m) {
                        return t[m.charCodeAt(0) & 15]
                    })
                }("v[x++]=v[--x]t.charCodeAt(b++)-32function return ))++.substrvar .length(),b+=;break;case ;break}".split("")))()('gr$Daten Иb/s!l y͒yĹg,(lfi~ah`{mv,-n|jqewVxp{rvmmx,&effkx[!cs"l".Pq%widthl"@q&heightl"vr*getContextx$"2d[!cs#l#,*;?|u.|uc{uq$fontl#vr(fillTextx$$龘ฑภ경2<[#c}l#2q*shadowBlurl#1q-shadowOffsetXl#$$limeq+shadowColorl#vr#arcx88802[%c}l#vr&strokex[ c}l"v,)}eOmyoZB]mx[ cs!0s$l$Pb<k7l l!r&lengthb%^l$1+s$jl  s#i$1ek1s$gr#tack4)zgr#tac$! +0o![#cj?o ]!l$b%s"o ]!l"l$b*b^0d#>>>s!0s%yA0s"l"l!r&lengthb<k+l"^l"1+s"jl  s&l&z0l!$ +["cs\'(0l#i\'1ps9wxb&s() &{s)/s(gr&Stringr,fromCharCodes)0s*yWl ._b&s o!])l l Jb<k$.aj;l .Tb<k$.gj/l .^b<k&i"-4j!+& s+yPo!]+s!l!l Hd>&l!l Bd>&+l!l <d>&+l!l 6d>&+l!l &+ s,y=o!o!]/q"13o!l q"10o!],l 2d>& s.{s-yMo!o!]0q"13o!]*Ld<l 4d#>>>b|s!o!l q"10o!],l!& s/yIo!o!].q"13o!],o!]*Jd<l 6d#>>>b|&o!]+l &+ s0l-l!&l-l!i\'1z141z4b/@d<l"b|&+l-l(l!b^&+l-l&zl\'g,)gk}ejo{cm,)|yn~Lij~em["cl$b%@d<l&zl\'l $ +["cl$b%b|&+l-l%8d<@b|l!b^&+ q$sign ', [Object.defineProperty(exports, '__esModule', {
                    value: !0
                })]);
            })
    }
    var installedModules = {};

    function __webpack_require__(moduleId) {
        // Check if module is in cache
        if (installedModules[moduleId]) {
            return installedModules[moduleId].exports;
        }
        // Create a new module (and put it into the cache)
        var module = installedModules[moduleId] = {
            i: moduleId,
            l: false,
            exports: {}
        };
        // Execute the module function
        modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
        // Flag the module as loaded
        module.l = true;
        // Return the exports of the module
        return module.exports;
    }

    var _bytedAcrawler = __webpack_require__("9bd2804c7e68ac461d65");
    var signature = _bytedAcrawler.sign(uid);
    return signature

}

_sign = get_signature("2471313590452925")
console.log(_sign)