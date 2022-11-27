----------------------------------------------------------------------------------
-- Company: 
-- Engineer: 
-- 
-- Create Date: 24.07.2022 21:33:01
-- Design Name: 
-- Module Name: FFT - Behavioral
-- Project Name: 
-- Target Devices: 
-- Tool Versions: 
-- Description: 
-- 
-- Dependencies: 
-- 
-- Revision:
-- Revision 0.01 - File Created
-- Additional Comments:
-- 
----------------------------------------------------------------------------------


library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
-- arithmetic functions with Signed or Unsigned values
use IEEE.NUMERIC_STD.ALL;
use work.config_const.all;
use work.types_pack.all;
-- Uncomment the following library declaration if using


-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity FFT is
    generic(N: integer range 0 to N  := 8);
    Port ( clk : in STD_LOGIC;
           rst: in std_logic;
           start : in std_logic;
           load_val: in std_logic;   
           x : in STD_LOGIC_VECTOR (26 downto 0);
           out_ready:out std_logic;
           F : out input_array;
           F_imag: out input_array);
end FFT;

architecture Behavioral of FFT is

component input_buffer_reg is
    generic(n:integer:=26);
    Port ( clk : in STD_LOGIC;
           rst: in STD_LOGIC;
           x : in STD_LOGIC_VECTOR (n downto 0);
           l_buffer : in STD_LOGIC;
           c_buffer : in STD_LOGIC;
           reg_output : out STD_LOGIC_VECTOR (n downto 0));
end component;

component bit_reversal is
    generic(N: integer:=8);
            
    Port ( inputs : in input_array;
           reversed : out input_array);
end component;

component fft_stages is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           start:in std_logic;
           RealVal : in input_array;
           ImagVal : in input_array;
           cnt     : in STD_LOGIC_VECTOR (N_size_bits-1 downto 0);
           ready : out STD_LOGIC;
           readyW : out STD_LOGIC;
           RealOut : out input_array;
           ImagOut : out input_array);
end component;


component counter is
    Port ( clk: in std_logic;
           rst_cnt : in STD_LOGIC;
           ld_cnt : in STD_LOGIC;
           cnt : out STD_LOGIC_VECTOR (N_size_bits-1 downto 0));
end component;

component start_ctrl_fsm is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           start : in STD_LOGIC;
           wready : in STD_LOGIC;
           cnt : in STD_LOGIC_VECTOR (N_size_bits-1 downto 0);
           stage_ready : in STD_LOGIC;
           store_stage : out STD_LOGIC;
           clr_cnt : out STD_LOGIC;
           ld_cnt : out STD_LOGIC;
           ld_new_val_real : out STD_LOGIC;
           ld_new_val_imag : out STD_LOGIC;
           start_comp : out STD_LOGIC;
           clr_real_imag : out STD_LOGIC);
end component;

type input_connection_array is array (0 to N-1) of std_logic_vector(26 downto 0);
signal buff_connection, buff_connection2,sreversed_inputs_aux,sreversed_inputs,simag_out,simag_in,sRealOut: input_array;
signal sclear_buff,sstart,sready,swready: std_logic;
signal sreg_output :STD_LOGIC_VECTOR (26 downto 0);

signal scnt:STD_LOGIC_VECTOR (N_size_bits-1 downto 0);
signal srst_cnt,sld_cnt:std_logic;



signal sclr_real_imag,sstore_stage,sld_new_val_real,sld_new_val_imag:std_logic;



begin

first_input:  input_buffer_reg port map( clk       =>clk, 
                                                        rst       =>rst,
                                                        x         =>x,
                                                        l_buffer  =>load_val,
                                                        c_buffer  =>sclear_buff,
                                                        reg_output=>buff_connection(0));

input_bufxx: for i in 1 to N-1 generate
                input_bufx:  input_buffer_reg port map( clk       =>clk, 
                                                        rst       =>rst,
                                                        x         =>buff_connection(i-1),
                                                        l_buffer  =>load_val,
                                                        c_buffer  =>sclear_buff,
                                                        reg_output=>buff_connection(i));        
            end generate;
            
            
imag_buff: for i in 0 to N-1 generate
                imag_buffx:  input_buffer_reg port map( clk       =>clk, 
                                                        rst       =>rst,
                                                        x         =>simag_out(i),
                                                        l_buffer  =>sld_new_val_imag,
                                                        c_buffer  =>sclr_real_imag,
                                                        reg_output=>simag_in(i));        
            end generate;

reverter: bit_reversal Port map(  inputs   => buff_connection,
                                  reversed => sreversed_inputs_aux);            


reversed_input_bufxx: for i in 0 to N-1 generate
                input_bufx:  input_buffer_reg port map( clk       =>clk, 
                                                        rst       =>rst,
                                                        x         =>sreversed_inputs(i),
                                                        l_buffer  =>sld_new_val_real,
                                                        c_buffer  =>sclr_real_imag,
                                                        reg_output=>buff_connection2(i));        
            end generate;

F<=sRealOut;


stages:fft_stages Port map(    clk    =>clk,
                               rst    =>rst,
                               start  =>sstart,
                               RealVal=>buff_connection2,
                               ImagVal=>simag_in,
                               cnt    =>scnt,
                               ready  =>sready,
                               readyW  =>swready,
                               RealOut=>sRealOut,
                               ImagOut=>simag_out);

cnt_counter:counter Port map(   clk     =>clk,
                                rst_cnt =>srst_cnt,
                                ld_cnt  =>sld_cnt,
                                cnt     =>scnt);


fsm:start_ctrl_fsm Port map(   clk             =>clk,
                               rst             =>rst,
                               start           =>start,
                               wready          =>swready,
                               cnt             =>scnt,
                               stage_ready     =>sready,
                               store_stage     =>sstore_stage,
                               clr_cnt         =>srst_cnt,
                               ld_cnt          =>sld_cnt,
                               ld_new_val_real =>sld_new_val_real,
                               ld_new_val_imag =>sld_new_val_imag,
                               start_comp      =>sstart,
                               clr_real_imag   =>sclr_real_imag);


sclear_buff<=rst;
F_imag<=simag_out;

with sstore_stage  select sreversed_inputs<=
    sRealOut when '0',
    sreversed_inputs_aux when others;


process(sready,scnt)
begin
    if unsigned(scnt)=N_size_bits-1 and sready='1' then 
        out_ready<= '1';
    else
        out_ready<='0';
    end if;
end process;


end Behavioral;
