import streamlit as st
st.set_page_config(layout='wide')
def principal():
    st.title('ROHP')
    st.write('''A ferramenta ROHP é uma ferramenta que realizará o diagnóstico de sua organização/setor a fim de conhecer sua situação atual, isto é, qual é o seu grau de maturidade em Gestão de Conhecimento (GC) e, assim, possa definir seu planejamento para implementar ou aperfeiçoar a GC.''')
    st.subheader('Instruções para preenchimento')
    '''Cada uma das 8 características presentes nas 4 dimensões deve ser minuciosamente analisada e pontuada com base em evidências, utilizando a seguinte escala:
    \n\n1= Discordo Totalmente
    \n2= Discordo
    \n3= Discordo Parcialmente
    \n4= Concordo
    \n5= Concordo Totalmente
    '''
    st.write('##')

    if st.button('Iniciar diagnóstico'):
        diagnostico()

def diagnostico():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Relacional')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Conduta ética**')
            st.write('Os servidores detém total conhecimento sobre os conceitos envolvidos nas condutas éticas e sempre os aplicam.')    
        with c2:
            conduta_etica = st.radio('',(1,2,3,4,5), key='conduta', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Transmissão de conhecimentos e experiências via rede**')
            st.write('Existe um canal de transmissão do conhecimento e troca de experiências entre os militares do setor bem como das demais áreas interessadas e este canal sempre é utilizado.')    
        with c2:
            transmissao_conhecimento = st.radio('',[1,2,3,4,5], key='transmissao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comunicação**')
            st.write('A comunicação entre os servidores do setor, bem como das demais áreas interessadas ocorre sem falhas e de forma objetiva.')    
        with c2:
            comunicacao = st.radio('',[1,2,3,4,5], key='comunicacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Práticas de integração**')
            st.write('São realizados eventos que permitem a integração entre a tripulação.')    
        with c2:
            praticas_integracao = st.radio('',[1,2,3,4,5], key='praticas', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Integração entre setores**')
            st.write('Os setores são totalmente integrados entre si, ou seja, os setores se complementam em busca do alcance da missão da OM.')    
        with c2:
            integracao_setores = st.radio('',[1,2,3,4,5], key='integracao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integração com organizações participantes**')
            st.write('Existe um programa bem definido e atualizado sobre a integração entre a OM apoiadora e as demais OM apoiadas.')    
        with c2:
            programa_integracao = st.radio('',[1,2,3,4,5], key='programa', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Comprometimento de todos os valores e comportamentos éticos na organização**')
            st.write('É visível o comprometimento de todos os envolvidos no processo com os valores e comportamentos éticos na oraganização.')    
        with c2:
            comprometimento = st.radio('',[1,2,3,4,5], key='comprometimento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de integridade**')
            st.write('Todos os envolvidos conhecem e prezam pelo Programa de Integridade da Marinha do Brasil.')    
        with c2:
            integridade = st.radio('',[1,2,3,4,5], key='integridade', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            organizacional()
        elif voltar:
            principal()            
         
        
def organizacional():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Organizacional')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Ambiente propício (disseminação de conhecimento**')
            st.write(' Esta Organização apresenta um ambiente totalmente propício para a Disseminação de conhecimento.')    
        with c2:
            ambiente_propicio = st.radio('',(1,2,3,4,5), key='ambiente_propicio', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Infraestrutura física e de processo**')
            st.write('A infraestrutura física e de processo são perfeitamente apropriadas para o alcance da Gestão do Conhecimento.')    
        with c2:
            infraestrutura = st.radio('',[1,2,3,4,5], key='infraestrutura', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Liderança formalmente estabelecidas (impoulsionadores da rede)**')
            st.write('As lideranças formalmente estabelecidas nos setores envolvidos impulsionam a rede de conhecimento?')    
        with c2:
            liderança = st.radio('',[1,2,3,4,5], key='lideranca', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estrutura de comunicação estabelecida**')
            st.write('Existe uma perfeita estrutura de comunicação estabelecida entre os setores.')    
        with c2:
            estrutura_comunicacao = st.radio('',[1,2,3,4,5], key='estrutura_comunicacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Design (TMFT = Regimento iterno)**')
            st.write('A TMFT está organizada de forma a permitir o melhor funcionamento dos setores da OM.')    
        with c2:
            design = st.radio('',[1,2,3,4,5], key='design', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Alinhamento objetivos estratégicos**')
            st.write('Todas as ações executadas pelos setores visam sempre o alcance dos objetivos estratégicos da OM.')    
        with c2:
            alinhamento = st.radio('',[1,2,3,4,5], key='alinhamento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Normas e valores comunicados**')
            st.write('As normas e os valores da OM são comunicados de forma abrangente para alcançar a todos os envolvidos.')    
        with c2:
            normas = st.radio('',[1,2,3,4,5], key='normas', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estrutura de papéis e responsabilidades**')
            st.write('Existe uma formalização da estrutura de funções e responsabilidades e esta formalização é divulgada para todos os envolvidos.')    
        with c2:
            estrutura = st.radio('',[1,2,3,4,5], key='estrutura', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            humana()
        elif voltar:
            diagnostico() 

def humana():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Humana')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Educação Formal**')
            st.write('A educação formal, ou seja, a educação proveniente do período educacional escolar, dos militares e civis envolvidos é adequada.')    
        with c2:
            educacao = st.radio('',(1,2,3,4,5), key='educacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Treinamento continuado**')
            st.write('A Organização possui calendário rotineiro de treinamentos e estimula a participação das pessoas.')    
        with c2:
            treinamento = st.radio('',[1,2,3,4,5], key='treinamento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Perfil da tripulação: Aproveitamento de conhecimentos e experiências**')
            st.write('A tripulação como um todo possui um perfil de aproveitamento adequado dos conhecimentos e experiências geradas.')    
        with c2:
            perfil = st.radio('',[1,2,3,4,5], key='perfil', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Formação dos instrutores internos**')
            st.write('As pessoas responsáveis por realizar treinamentos internos com a tripulação possui formação adequada.')    
        with c2:
            formacao = st.radio('',[1,2,3,4,5], key='formacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de desenvolvimento de liderança**')
            st.write('A OM busca estimular o programa de desenvolvimento de liderança, ou seja, mostra uma preocupação com o aprendizado das habilidades e competências de líderes, seja Oficial ou Praça.')    
        with c2:
            programa = st.radio('',[1,2,3,4,5], key='programa', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Preocupação com aspectos motivacionais**')
            st.write('As pessoas investidas de função de liderança demonstra total preocupação com aspectos motivacionais.')    
        with c2:
            preocupacao = st.radio('',[1,2,3,4,5], key='preocupacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Estímulos à criatividade**')
            st.write('As pessoas investidas de função de liderança, seja Oficial ou Praça, demonstram estímulo à criatividade.')    
        with c2:
            estimulos = st.radio('',[1,2,3,4,5], key='estimulos', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Incentivo ao comprometimento**')
            st.write('As pessoas investidas de função de liderança, seja Oficial ou Praça, demonstram total incentivo ao comprometimento perante a missão da OM.')    
        with c2:
            incentivo = st.radio('',[1,2,3,4,5], key='incentivo', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            processual()
        elif voltar:
            organizacional() 

def processual():
    st.title('Diagnóstico')
    st.write('')

    with st.form('ROHP'):
        st.subheader('Dimensão Processual')
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Sistematização de conhecimento**')
            st.write('O conhecimento está sistematizado, ou seja, está ordenado, classificado e baseado em um parâmetro para atingir ao objetivo proposto.')    
        with c2:
            sistematizacao = st.radio('',(1,2,3,4,5), key='sistematizacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Práticas e processos de captação de pessoal (Mapa de competências)**')
            st.write('Existem procedimentos de práticas e processos de captação de pessoal bem definidos e atualizados, como por exemplo, mapas de competências das pessoas que servem na OM.')    
        with c2:
            praticas_competencia = st.radio('',[1,2,3,4,5], key='praticas_competencia', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Processo de codificação**')
            st.write('Existem métodos e incentivos para melhorar a codificação do conhecimento, ou seja, formas de facilitar o aprendizado e conhecimento.')    
        with c2:
            processo_codificacao = st.radio('',[1,2,3,4,5], key='processo_codificacao', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Conhecimento institucionalizados e experiências codificadas**')
            st.write('Os conhecimentos atinentes ao setor estão institucionalizados e as experiências adquiridas estão codificadas, de maneira a facilitar o compartilhamento')    
        with c2:
            conhecimento = st.radio('',[1,2,3,4,5], key='conhecimento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Programa de desenvolvimento de competências: Esforço em pesquisa e desenvolvimento**')
            st.write('A OM sempre incentiva a área da pesquisa e desenvolvimento visando o desenvolvimento de competências. (Entende-se por desenvolvimento de competências a aquisição do conhecimento e o domínio das habilidades necessárias para desempenhar o seu papel).')    
        with c2:
            programa_competencia = st.radio('',[1,2,3,4,5], key='programa_competencia', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Uso de TIC para a gestão do conhecimento**')
            st.write('Existem recursos tecnológicos direcionados para a Gestão do conhecimento.')    
        with c2:
            tic = st.radio('',[1,2,3,4,5], key='tic', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Gestão Documental**')
            st.write('O Setor possui uma Gestão efetiva de documentos. (Considere Gestão de documentos a Organização, produção, uso e destinação dos documentos, de forma a tornar a informação mais acessível e sua guarda sustentável).')    
        with c2:
            gestao_doc = st.radio('',[1,2,3,4,5], key='gestao_doc', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2 = st.columns([6,2])
        with c1:
            st.write('**Mapeamento de Processos**')
            st.write('Os processos existentes estão inteiramente mapeados e atualizados.')    
        with c2:
            mapeamento = st.radio('',[1,2,3,4,5], key='mapeamento', horizontal=True)
        st.markdown('<hr>', unsafe_allow_html=True)
        c1,c2,c3=st.columns([1,10,1])
        with c1:
            voltar = st.form_submit_button('Voltar')
        with c2:
            st.write('')
        with c3:
            avancar = st.form_submit_button('Avançar')
        if avancar: 
            relatorio()
        elif voltar:
            humana() 

def relatorio():
    pass

principal()