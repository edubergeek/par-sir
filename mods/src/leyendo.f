        subroutine leyendo !carga en commons toda la informacion necesaria
               
c para definir los datos de entrada
        character*100 mallaobs
        character*100 nomlineas,fichabun,modelname
        character*100 Stokesfilename
        logical ex        
        real*4 eps(92)
                       
c lugares comunes de memoria para 
        common/ficlineas/nomlineas           !para leelineasii (en StokesFRsub)
        common/fichabun/fichabun
        common/OutputStokes/Stokesfilename   !para escribe_Stokes
        common/abundances/eps
        
c nombre del fichero con los parametros atomicos
        nomlineas='LINEAS'
        
c nombre del fichero con las abundancias
        !fichabun='THEVENIN'        

        !call leeabun(0,eps)        
        eps(1)  =12.0
        eps(2)  =11.0
        eps(3)  =0.60
        eps(4)  =1.35
        eps(5)  =-8.0
        eps(6)  =8.55
        eps(7)  =7.93
        eps(8)  =8.77
        eps(9)  =5.40
        eps(10) =8.51
        eps(11) =6.18
        eps(12) =7.48
        eps(13) =6.40
        eps(14) =7.55
        eps(15) =5.51
        eps(16) =7.21
        eps(17) =5.40
        eps(18) =6.62
        eps(19) =5.05
        eps(20) =6.33
        eps(21) =3.20
        eps(22) =4.28
        eps(23) =3.66
        eps(24) =5.47
        eps(25) =4.88
        eps(26) =7.50
        eps(27) =4.30
        eps(28) =5.08
        eps(29) =3.88
        eps(30) =3.98
        eps(31) =2.31
        eps(32) =2.43
        eps(33) =-8.0
        eps(34) =-8.0
        eps(35) =-8.0
        eps(36) =-8.0
        eps(37) =2.81
        eps(38) =3.08
        eps(39) =2.80
        eps(40) =2.38
        eps(41) =1.98
        eps(42) =2.08
        eps(43) =-8.0
        eps(44) =1.75
        eps(45) =1.73
        eps(46) =1.78
        eps(47) =0.85
        eps(48) =2.05
        eps(49) =1.69
        eps(50) =-8.0
        eps(51) =0.93
        eps(52) =-8.0
        eps(53) =-8.0
        eps(54) =-8.0
        eps(55) =2.38
        eps(56) =2.88
        eps(57) =1.68
        eps(58) =1.71
        eps(59) =0.77
        eps(60) =1.91
        eps(61) =-8.0
        eps(62) =1.18
        eps(63) =1.14
        eps(64) =1.31
        eps(65) =1.47
        eps(66) =0.53
        eps(67) =1.61
        eps(68) =1.98
        eps(69) =1.31
        eps(70) =1.99
        eps(71) =1.29
        eps(72) =1.13
        eps(73) =1.98
        eps(74) =1.33
        eps(75) =2.13
        eps(76) =1.63
        eps(77) =2.43
        eps(78) =1.93
        eps(79) =0.50
        eps(80) =1.98
        eps(81) =-8.0
        eps(82) =1.98
        eps(83) =1.63
        eps(84) =-8.0
        eps(85) =-8.0
        eps(86) =-8.0
        eps(87) =-8.0
        eps(88) =-8.0
        eps(89) =-8.0
        eps(90) =1.21
        eps(91) =-8.0
        eps(92) =1.48




c leemos la malla  
        mallaobs='malla.grid'
        call lee_malla(mallaobs)     ! carga el common Malla/ntl,nlin,npas,nble,dlamda
                          
c nombre del fichero de salida con los perfiles de Stokes        
        Stokesfilename='perfil.per'        
        
        return      
        end
