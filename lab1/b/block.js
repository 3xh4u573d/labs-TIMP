(()=>{//анонимная функция для предотвращения доступа к переменным из консоли
    let simpleHash = function(s) {
        var a = 1, c = 0, h, o;
        if (s) {
            a = 0;
            for (h = s.length - 1; h >= 0; h--) {
                o = s.charCodeAt(h);
                a = (a<<6&268435455) + o + (o<<14);
                c = a & 266338304;
                a = c!==0?a^c>>21:a;
            }
        }
        return a;
    };
    var access = false

    let noselect = () => access
    let antiDebug = setInterval(()=>{ //Запрет на дебаг js кода
        debugger;
    },10)
    document.ondragstart = noselect //Запрещаем выделять текст
    document.onselectstart = noselect
    document.oncontextmenu = noselect

    document.addEventListener("keydown", function(event) {
        if (event.altKey && event.code === "KeyX")  {//По Alt+X показываем ввод пароля
            const pass = prompt("Введите пароль:")
            access = checkPassword(pass)
            if (access) clearInterval(antiDebug)
        } else if (event.ctrlKey && event.code === "KeyS"
                  || (event.keyCode >=112 && event.keyCode <= 123) )  {//Запрещаем сохранять страницу через Ctrl+S,а также все кнопки F1-F12, в особенности devTools (F12)
            if (access) return true;
            event.preventDefault();
            return false;
        }
    });

    let checkPassword = (pass) => simpleHash(pass) == 179310630; //super$hard$pass93
    document.addEventListener('copy', function(e){ //Запрещаем копировать
        if (access) return true;
        e.clipboardData.setData('text/plain', '');
        e.preventDefault();
    });
})()