# Dump all variables to a file on the target machine

Add this task to your playbook:

```
    tasks:
      - name: dump all vars
        action: template src=templates/dumpall.j2 dest=/tmp/ansible.all
```

Then use this template file 'dumpall.j2':


```
    Module Variables ("vars"):
    --------------------------------
    {{ vars | to_nice_json }} 

    Environment Variables ("environment"):
    --------------------------------
    {{ environment | to_nice_json }} 

    GROUP NAMES Variables ("group_names"):
    --------------------------------
    {{ group_names | to_nice_json }}

    GROUPS Variables ("groups"):
    --------------------------------
    {{ groups | to_nice_json }}

    HOST Variables ("hostvars"):
    --------------------------------
    {{ hostvars | to_nice_json }} 
```

