create database dados;
use dados;

create table dados_conta(
titular varchar(50),
agencia varchar(8),
conta varchar(11) primary key,
senha varchar(10),
saldo float(2)
);


create table dados_extrato(
conta varchar(11),
movimentacao varchar(80),
data_mov varchar(30)
);

alter table chaves_pix
	modify column conta varchar(11) primary key;

create table chaves_pix(
conta varchar(11) primary key,
cpf_pix varchar(15),
celular_pix varchar(15),
email_pix varcharacter(30)
);

drop database dados;
drop table dados_conta;
select * from dados_conta;

drop table chaves_pix;