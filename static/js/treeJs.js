$(document).ready(function() {
            $('nav ul li.has-submenu > a').click(function(e) {
                e.preventDefault();
                var submenu = $(this).siblings('ul');
                
                // Если подменю уже открыто, закрываем его
                if (submenu.is(':visible')) {
                    submenu.slideUp();
                    $(this).parent().removeClass('active');
                } else {
                    // Закрываем все другие подменю и отменяем класс active
                    $('nav ul li.has-submenu > ul').slideUp();
                    $('nav ul li.has-submenu').removeClass('active');
                    
                    // Открываем текущее подменю
                    submenu.slideDown();
                    $(this).parent().addClass('active');
                }
            });

            $(document).click(function(e) {
                var container = $('nav ul li.has-submenu');
                
                // Если клик был не по меню, закрываем подменю
                if (!container.is(e.target) && container.has(e.target).length === 0) {
                    $('nav ul li.has-submenu > ul').slideUp();
                    $('nav ul li.has-submenu').removeClass('active');
                }
            });
        });