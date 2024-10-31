$(document).ready(function() {
        // Проверка jQuery
        console.log("jQuery is working!");

        $('#id_vacation_date_start').datepicker({
            dateFormat: 'yy-mm-dd',
            onClose: function(selectedDate) {
                $('#id_vacation_date_end').datepicker(
                    "option",
                    "minDate",
                    selectedDate
                );
                validateDates();
            }
        });
        $('#id_vacation_date_end').datepicker({
            dateFormat: 'yy-mm-dd',
            onClose: function(selectedDate) {
                $('#id_vacation_date_start').datepicker(
                    "option",
                    "maxDate",
                    selectedDate
                );
                validateDates();
            }
            
        });

        function validateDates() {
            var startDate = $('#id_vacation_date_start').val();
            var endDate = $('#id_vacation_date_end').val();

            if (startDate && endDate) {
                if (new Date(startDate) >= new Date(endDate)) {
                    alert("Дата начала отпуска не может быть позже даты окончания");
                    $('#id_vacation_date_start').val('');
                    $('#id_vacation_date_end').val('');
                }
            }
        }
    });