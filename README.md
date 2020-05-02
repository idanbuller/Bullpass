# Bullpass

Bull pass is an updating project of password generator framework.

## New


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 1

Enter password length: 10
+--------------+------------+
|  -- OK? --   |     --     |
+--------------+------------+
| New Password | H6mPF$BxqU |
+--------------+------------+

[Y/n]y

Enter the website's name: site4

Enter the user name: user4

Row added -
('site4', 'user4', 'H6mPF$BxqU', 11)

Password copied to clipboard!

```


## Old


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 2

Type your password: 
password5

Enter the website's name: site5

Enter the user name: user5

Row added -
('site5', 'user5', 'password5', 12)

Password copied to clipboard!
```

## Search


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 3
+------+------+----------+
| Site | User | Password |
+------+------+----------+
|  1   |  2   |    3     |
+------+------+----------+
>> Enter Your Choice: 1
>> Enter SITE name: site1
+-------+-------+-----------+---+
| site1 | user1 | password1 | 1 |
+-------+-------+-----------+---+
```

## Show


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 4
+-------+-------+------------+----+
| site1 | user1 | password1  |  1 |
| site2 | user2 | password2  |  2 |
| site3 | user3 | password3  |  3 |
| site4 | user4 | H6mPF$BxqU | 11 |
| site5 | user5 | password5  | 12 |
+-------+-------+------------+----+
```

## Delete


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 5
Choose row to delete by ID -
+-------+-------+------------+----+
| site1 | user1 | password1  |  1 |
| site2 | user2 | password2  |  2 |
| site3 | user3 | password3  |  3 |
| site4 | user4 | H6mPF$BxqU | 11 |
| site5 | user5 | password5  | 12 |
+-------+-------+------------+----+
>> Enter id: 12

Row Deleted -
('site5', 'user5', 'password5', 12)
```

## Update


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 6
+------+------+----------+
| Site | User | Password |
+------+------+----------+
|  1   |  2   |    3     |
+------+------+----------+
>> Enter Your Choice: 1
>> Enter SITE name to change: site4
>> Enter new SITE name: site5

Row Updated -
('site5', 'user4', 'H6mPF$BxqU', 11)
```

## Export


```
+-----+-----+--------+------+--------+--------+--------+
| NEW | OLD | Search | Show | Delete | UPDATE | Export |
+-----+-----+--------+------+--------+--------+--------+
|  1  |  2  |   3    |  4   |   5    |   6    |   7    |
+-----+-----+--------+------+--------+--------+--------+
>> Enter Your Choice (b = back): 7
File passwords.csv created!
```
