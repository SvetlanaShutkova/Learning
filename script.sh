while true
do
        echo "enter your name:"
        read name
        if [ -z $name ]
        then
                echo "bye"
                break
        fi
        echo "enter your age:"
        read age
        if [[ $age -le 16 && $age -gt 0 ]]
        then
                echo "$name, your group is child"
        elif [[ $age -ge 17 && $age -le 25 ]]
        then
                echo "$name, your group is youth"
        elif [[ $age -gt 25 ]]
        then
                echo "$name, your group is adult"
        else
                echo "bye"
                break
        fi
done
